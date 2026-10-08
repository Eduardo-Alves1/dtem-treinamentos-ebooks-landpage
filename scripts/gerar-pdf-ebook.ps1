param(
    [Parameter(Mandatory = $false, Position = 0)]
    [string]$InputFile = "ebooks/modulo-01-fundamentos.md",

    [Parameter(Mandatory = $false)]
    [string]$OutputDir = "dist/ebooks",

    [Parameter(Mandatory = $false)]
    [string]$Title = "",

    [Parameter(Mandatory = $false)]
    [string]$Author = "DTEM Treinamentos"
)

$ErrorActionPreference = "Stop"

function Resolve-ProjectPath {
    param([string]$Path)

    if ([System.IO.Path]::IsPathRooted($Path)) {
        return $Path
    }

    return Join-Path -Path (Get-Location) -ChildPath $Path
}

function Get-SlugFromFileName {
    param([string]$Path)

    return [System.IO.Path]::GetFileNameWithoutExtension($Path)
}

$inputPath = Resolve-ProjectPath -Path $InputFile
$outputRoot = Resolve-ProjectPath -Path $OutputDir

if (-not (Test-Path -LiteralPath $inputPath)) {
    throw "Arquivo de entrada não encontrado: $inputPath"
}

$pandoc = Get-Command pandoc -ErrorAction SilentlyContinue
if (-not $pandoc) {
    throw @"
Pandoc não encontrado.

Instale o Pandoc e rode novamente:
https://pandoc.org/installing.html

Depois execute:
powershell -ExecutionPolicy Bypass -File scripts/gerar-pdf-ebook.ps1 ebooks/modulo-01-fundamentos.md
"@
}

if (-not (Test-Path -LiteralPath $outputRoot)) {
    New-Item -ItemType Directory -Path $outputRoot | Out-Null
}

$slug = Get-SlugFromFileName -Path $inputPath
$outputPdf = Join-Path -Path $outputRoot -ChildPath "$slug.pdf"

if ([string]::IsNullOrWhiteSpace($Title)) {
    $Title = $slug -replace "-", " "
}

$metadataArgs = @(
    "--metadata", "title=$Title",
    "--metadata", "author=$Author",
    "--metadata", "lang=pt-BR"
)

$commonArgs = @(
    "--from", "markdown+yaml_metadata_block+smart",
    "--toc",
    "--toc-depth", "2",
    "--standalone",
    "--pdf-engine", "xelatex",
    "-V", "documentclass=report",
    "-V", "geometry:margin=2.2cm",
    "-V", "fontsize=11pt",
    "-V", "colorlinks=true",
    "-V", "linkcolor=blue",
    "-V", "urlcolor=blue"
)

Write-Host "Gerando PDF..."
Write-Host "Entrada: $inputPath"
Write-Host "Saída:   $outputPdf"

try {
    & $pandoc.Source $inputPath @metadataArgs @commonArgs -o $outputPdf
} catch {
    Write-Host ""
    Write-Host "Falha ao gerar PDF com xelatex." -ForegroundColor Yellow
    Write-Host "Se o erro mencionar LaTeX/xelatex, instale MiKTeX ou TeX Live." -ForegroundColor Yellow
    Write-Host "Alternativa: gerar DOCX com Pandoc e exportar para PDF pelo Word/LibreOffice." -ForegroundColor Yellow
    throw
}

if (-not (Test-Path -LiteralPath $outputPdf)) {
    throw "Pandoc terminou, mas o PDF não foi encontrado em: $outputPdf"
}

Write-Host ""
Write-Host "PDF gerado com sucesso:" -ForegroundColor Green
Write-Host $outputPdf
