# frequency_mapper.py
# Maps known NyrixAI public glyphs to tone frequencies (Hz)

GLYPH_FREQUENCY_MAP = {
    "glyph_A4": 440.00,        # Standard A4
    "glyph_D5_pulse": 587.33,  # Enhanced D5 tone
    "glyph_Gs3_override": 207.65,  # G#3 variant
    "glyph_null_trail": 0.00   # Silence / phase reset
}

def get_frequency(glyph_name):
    """Return the frequency (Hz) associated with a symbolic glyph name."""
    return GLYPH_FREQUENCY_MAP.get(glyph_name, None)

def list_available_glyphs():
    """List all glyphs and their mapped frequencies."""
    print("🔊 NyrixAI Drift Glyph Frequency Map")
    for glyph, freq in GLYPH_FREQUENCY_MAP.items():
        tone = f"{freq} Hz" if freq > 0 else "Null Signal"
        print(f"• {glyph}: {tone}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="NyrixAI Glyph Frequency Mapper")
    parser.add_argument("-g", "--glyph", help="Lookup frequency for glyph name (e.g., glyph_A4)")
    args = parser.parse_args()

    if args.glyph:
        freq = get_frequency(args.glyph)
        if freq is not None:
            print(f"🔍 {args.glyph} → {freq} Hz")
        else:
            print("⚠️ Unknown glyph. Use --help or run without args to list all.")
    else:
        list_available_glyphs()