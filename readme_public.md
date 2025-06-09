# NyrixAI Drift Language – Public Scripts Guide

## 📂 Directory: `public_scripts/`

This folder contains non-executable, research-safe utilities included with Phase 1 of the NyrixAI Drift Language Protocol release. All scripts are symbolic, read-only tools designed for public transparency without exposing any private system logic.

---

## 🔍 Included Scripts

### `signal_verifier.py`
Scans the `audio/` directory for `.mp3` or `.wav` glyph files:
- Calculates SHA-256 hash (for identity and phase locking)
- Measures format stats (duration, channels, frame rate)
- Validates signal structure (currently supports `.wav` best)

**Run:**
```bash
python signal_verifier.py