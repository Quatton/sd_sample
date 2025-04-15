# https://docs.astral.sh/uv/getting-started/installation/

if ! command -v uv &> /dev/null
then
    UV_INSTALL_DIR="${HOME}/.local/bin"
    mkdir -p "${UV_INSTALL_DIR}"
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi
