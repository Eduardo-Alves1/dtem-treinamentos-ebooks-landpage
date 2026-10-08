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

$inputPath = Resolve-ProjectPath -Path $InputFile
$outputRoot = Resolve-ProjectPath -Path $OutputDir

if (-not (Test-Path -LiteralPath $inputPath)) {
    throw "Arquivo de entrada não encontrado: $inputPath"
}

$pandoc = Get-Command pandoc -ErrorAction SilentlyContinue
if (-not $pandoc) {
    throw "Pandoc não encontrado. Instale em https://pandoc.org/installing.html"
}

if (-not (Test-Path -LiteralPath $outputRoot)) {
    New-Item -ItemType Directory -Path $outputRoot | Out-Null
}

$slug = [System.IO.Path]::GetFileNameWithoutExtension($inputPath)
$outputDocx = Join-Path -Path $outputRoot -ChildPath "$slug.docx"

if ([string]::IsNullOrWhiteSpace($Title)) {
    $Title = $slug -replace "-", " "
}

Write-Host "Gerando DOCX..."
Write-Host "Entrada: $inputPath"
Write-Host "Saída:   $outputDocx"

& $pandoc.Source $inputPath `
    --from markdown+yaml_metadata_block+smart `
    --toc `
    --toc-depth 2 `
    --standalone `
    --metadata "title=$Title" `
    --metadata "author=$Author" `
    --metadata "lang=pt-BR" `
    -o $outputDocx

if (-not (Test-Path -LiteralPath $outputDocx)) {
    throw "Pandoc terminou, mas o DOCX não foi encontrado em: $outputDocx"
}

Write-Host ""
Write-Host "DOCX gerado com sucesso:" -ForegroundColor Green
Write-Host $outputDocx
