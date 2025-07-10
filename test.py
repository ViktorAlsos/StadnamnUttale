import subprocess

def speak_norwegian_ipa_with_lexconvert(ipa_text: str):
    """
    Convert Norwegian IPA to espeak phonemes using lexconvert,
    then speak it with espeak-ng in Norwegian voice.
    
    Args:
        ipa_text (str): Unicode IPA string 
    """
    try:
        # Step 1: Convert IPA to espeak phonemes using lexconvert
        conversion = subprocess.run(
            ["python", "-m", "lexconvert", "--phones2phones", "unicode-ipa", "espeak", ipa_text],
            capture_output=True,
            text=True,
            check=True
        )

        espeak_phonemes = conversion.stdout.strip()
        print(f"[lexconvert] IPA → eSpeak phonemes: {espeak_phonemes}")

        # Step 2: Speak the phonemes with espeak-ng (Norwegian)
        subprocess.run(
            ["espeak-ng", "-v", "nb", "-x", espeak_phonemes],
            check=True
        )

    except subprocess.CalledProcessError as e:
        print("❌ Error during conversion or speech:\n", e.stderr or e)
    except FileNotFoundError as e:
        print("❌ Missing command (is espeak-ng and lexconvert installed?):", e)

# Example usage
speak_norwegian_ipa_with_lexconvert("grøːt")  

# [ˈʊʂlʊ]
# katt	[kɑtː]
# hund	[hʉnː]
# skole	[ˈskuːlə]
# bok	[buːk]
# vei	[ʋæɪ̯]
# hus	[hʉːs]
# kjøre	[ˈçøːrə]
# brød	[brøː]
# grøt	[grøːt]
