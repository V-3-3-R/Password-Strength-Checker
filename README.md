# 🔐 Password Strength Checker (Python)

**Robust, enterprise-grade password strength evaluation tool following NIST SP 800-63B guidelines.**  
Checks entropy, patterns, dictionary words, and character diversity — far more advanced than typical regex-based checkers.

Includes both **console mode** and an **interactive GUI for Jupyter/Colab**.  
Lightweight, dependency-free (except `ipywidgets` for GUI).

---

## 🚀 Features

- **Modular Rules Engine**  
  Configurable checks for:
  - Length  
  - Character diversity  
  - Shannon entropy  
  - Dictionary/common words  
  - Predictable patterns  

- **NIST-Inspired Scoring**  
  Passphrases are rewarded for randomness and usability  
  (e.g., _CorrectHorseBatteryStaple42!_ scores high).

- **Interactive GUI (Colab/Jupyter)**  
  Real-time feedback with widget-based UI.

- **Comprehensive Feedback**  
  Score (0–100), strength label, detailed suggestions, warnings.

- **Unit Tests Included**  
  Fully compatible with `unittest` / `pytest`.

- **Logging & Extensibility**  
  Add new rules or plug in APIs (e.g., Have I Been Pwned).

- **Lightweight**  
  ~200 LOC. No heavy dependencies.

---

## 📸 Quick Demo (Colab Recommended)

**Try the interactive version in Google Colab!**  
Just copy the `.ipynb` into a Colab cell — widgets render automatically.

### ✔ Good Password Example  
**BlueSkyRocketZebra7#**  
- Score: **100/100**  
- Strength: **Strong**

### ❌ Bad Password Example  
**password123**  
- Score: **20/100**  
- Strength: **Weak**

---

## 📦 Installation

### 🔧 Local Development

```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker
pip install ipywidgets
python src/checker.py
```

# 🧪 Jupyter / Google Colab

- No installation required.
- Just copy/paste the contents of PasswordStrengthChecker.ipynb into a Colab cell and run.

# 🖥 Usage
Console Mode (Basic / Advanced)
```bash
from src.checker import AdvancedPasswordChecker

config = {
    'min_length': 12,
    'min_entropy': 60.0,
    'common_words': ['password', 'google']
}

checker = AdvancedPasswordChecker(config)

password = "CorrectHorseBatteryStaple42!"
feedback = checker.check(password)

print(f"Strength: {feedback.strength} | Score: {feedback.score}/100")
```

# Output:
```bash
Strength: Strong | Score: 100.0/100
```

# GUI Mode (Jupyter/Colab)
Launch the interface:
```bash
checker.create_user_gui()
```
It includes:
- Constraints display (e.g., “Length ≥ 12”)
- Password input field
- Strength score visual output

To print constraints:
```bash
print(checker.get_constraints_text())
```

# ⚙️ Customization
- Add Your Own Rules
  - Subclass PasswordRule and add it to self.rules.
- Strict Security Mode
  - Increase entropy requirement, e.g.:
```bash
config['min_entropy'] = 80.0
```
- Production Tips
  - Hash password input before logging
  - Add rate-limiting
  - Integrate HaveIBeenPwned API
  - Disable GUI in deployment mode

# 🧪 Testing
Run all unit tests:
```bash
python -m unittest discover tests
```
The test suite includes:
- Weak password tests
- Strong password tests
- Entropy calculation
- Empty input handling

All tests pass with 100% coverage.
In Colab, the notebook auto-runs tests at the end.

# 🤝 Contributing
1. Fork the repo
2. Create a branch:
```bash
git checkout -b feature/amazing-rule
```
3. Commit your changes:
```bash
git commit -m "Add new rule"
```
4. Push:
```bash
git push origin feature/amazing-rule
```
5. Open a Pull Request 🚀

- Ideas welcome:
  - Streamlit / Flask web deployment
  - zxcvbn integration
  - Mobile version

# 📄 License
Licensed under the MIT License.
See the LICENSE file for details.

Made with ❤️ for secure digital habits.
