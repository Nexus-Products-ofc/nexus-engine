# GitHub Pages — Nexus Engine

## Site URL

After enabling Pages (one-time):

- **Home:** https://heitorhanzelgontijo-svg.github.io/nexus-engine/
- **Tutorial:** https://heitorhanzelgontijo-svg.github.io/nexus-engine/tutorial.html

## Enable (required once)

1. Open https://github.com/heitorhanzelgontijo-svg/nexus-engine/settings/pages
2. Under **Build and deployment** → **Source**, choose **GitHub Actions**
3. Open the **Actions** tab → workflow **Deploy GitHub Pages** → **Run workflow** (or push any change under `docs/website/`)

The workflow file is `.github/workflows/pages.yml` and publishes the folder `docs/website/`.

## Local preview

```bash
cd docs/website
python -m http.server 8080
```
