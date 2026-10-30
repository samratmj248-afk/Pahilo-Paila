/**
 * Pahilo Paila Montessori - Modern UI Engine & Interactions
 */

// Theme Settings (Child-Friendly Bright Montessori Theme)
function initTheme() {
  document.documentElement.setAttribute('data-theme', 'light');
  localStorage.setItem('pahilo-theme', 'light');
}

function toggleTheme() {
  document.documentElement.setAttribute('data-theme', 'light');
}

function updateThemeIcon(theme) {
  const themeBtns = document.querySelectorAll('.theme-toggle-btn');
  themeBtns.forEach(btn => {
    if (theme === 'light') {
      btn.innerHTML = '<i class="bi bi-moon-stars-fill text-warning"></i>';
      btn.setAttribute('title', 'Switch to Dark Mode');
    } else {
      btn.innerHTML = '<i class="bi bi-sun-fill text-warning"></i>';
      btn.setAttribute('title', 'Switch to Light Mode');
    }
  });
}

// Service Worker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(reg => console.log('[PWA] Service Worker registered:', reg.scope))
      .catch(err => console.warn('[PWA] Registration failed:', err));
  });
}

// PWA Install Detection & Strict Auto-Hide
let deferredPrompt;
const pwaItem = document.getElementById('floating-pwa-item');
const pwaCircleBtn = document.getElementById('pwa-circle-btn');
const pwaHoverInstallBtn = document.getElementById('pwa-hover-install-btn');

function checkPWAInstalledStatus() {
  const isStandalone = window.navigator.standalone === true || 
                       window.matchMedia('(display-mode: standalone)').matches ||
                       localStorage.getItem('pahilo-pwa-installed') === 'true';
  if (isStandalone && pwaItem) {
    pwaItem.style.display = 'none';
  }
}
checkPWAInstalledStatus();

window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPrompt = e;
  if (pwaItem && localStorage.getItem('pahilo-pwa-installed') !== 'true') {
    pwaItem.style.display = 'block';
  }
});

window.addEventListener('appinstalled', () => {
  console.log('[PWA] Pahilo Paila App successfully installed!');
  localStorage.setItem('pahilo-pwa-installed', 'true');
  if (pwaItem) pwaItem.style.display = 'none';
  deferredPrompt = null;
});

async function triggerInstallPrompt() {
  if (deferredPrompt) {
    deferredPrompt.prompt();
    const { outcome } = await deferredPrompt.userChoice;
    console.log(`[PWA] Install prompt outcome: ${outcome}`);
    if (outcome === 'accepted') {
      localStorage.setItem('pahilo-pwa-installed', 'true');
      if (pwaItem) pwaItem.style.display = 'none';
    }
    deferredPrompt = null;
  } else {
    alert('Pahilo Paila App is ready or already installed on your device!');
  }
}

if (pwaCircleBtn) pwaCircleBtn.addEventListener('click', triggerInstallPrompt);
if (pwaHoverInstallBtn) pwaHoverInstallBtn.addEventListener('click', triggerInstallPrompt);

// ==================== AMAZING BALLOON BURST & SOUND ENGINE ====================
let audioCtx = null;

function playBalloonPopSound() {
  try {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;
    if (!audioCtx) audioCtx = new AudioContext();
    if (audioCtx.state === 'suspended') audioCtx.resume();

    // Layer 1: Crisp Sharp Pop / Burst Impact
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(420, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(80, audioCtx.currentTime + 0.12);

    gain.gain.setValueAtTime(0.8, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.12);

    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + 0.13);

    // Layer 2: Joyful High Chime / Sparkle
    const chimeOsc = audioCtx.createOscillator();
    const chimeGain = audioCtx.createGain();
    chimeOsc.type = 'sine';
    const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
    const randomNote = notes[Math.floor(Math.random() * notes.length)];
    chimeOsc.frequency.setValueAtTime(randomNote, audioCtx.currentTime);
    chimeOsc.frequency.exponentialRampToValueAtTime(randomNote * 1.5, audioCtx.currentTime + 0.25);

    chimeGain.gain.setValueAtTime(0.35, audioCtx.currentTime);
    chimeGain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.28);

    chimeOsc.connect(chimeGain);
    chimeGain.connect(audioCtx.destination);
    chimeOsc.start();
    chimeOsc.stop(audioCtx.currentTime + 0.3);
  } catch (err) {
    console.log('Audio pop effect:', err);
  }
}

// Advanced AI Phonics & Vocabulary Engine for Montessori Balloons
const BALLOON_VOCABULARY = {
  'A': { word: 'Apple', phrase: 'A for Apple! 🍎', speech: 'A for Apple! Good job!', lang: 'en-US', icon: '🍎' },
  'B': { word: 'Ball', phrase: 'B for Ball! ⚽', speech: 'B for Ball! Well done!', lang: 'en-US', icon: '⚽' },
  'C': { word: 'Cat', phrase: 'C for Cat! 🐱', speech: 'C for Cat! Meow!', lang: 'en-US', icon: '🐱' },
  'D': { word: 'Duck', phrase: 'D for Duck! 🦆', speech: 'D for Duck! Quack quack!', lang: 'en-US', icon: '🦆' },
  'E': { word: 'Elephant', phrase: 'E for Elephant! 🐘', speech: 'E for Elephant! Wonderful!', lang: 'en-US', icon: '🐘' },
  'क': { word: 'कमल', phrase: 'क बाट कमल! 🌸', speech: 'क बाट कमल! धेरै राम्रो!', lang: 'ne-NP', icon: '🌸' },
  'ख': { word: 'खरायो', phrase: 'ख बाट खरायो! 🐰', speech: 'ख बाट खरायो! कति ज्ञानी!', lang: 'ne-NP', icon: '🐰' },
  'ग': { word: 'गाई', phrase: 'ग बाट गाई! 🐄', speech: 'ग बाट गाई! बाच्छा र गाई!', lang: 'ne-NP', icon: '🐄' },
  'घ': { word: 'घर', phrase: 'घ बाट घर! 🏠', speech: 'घ बाट घर! हाम्रो प्यारो घर!', lang: 'ne-NP', icon: '🏠' },
  'ङ': { word: 'ङ', phrase: 'ङ अक्षर! 🌟', speech: 'ङ अक्षर! स्याबास!', lang: 'ne-NP', icon: '🌟' },
  '1': { word: 'One', phrase: 'Number 1! Star ⭐', speech: 'Number One! One little star!', lang: 'en-US', icon: '⭐' },
  '2': { word: 'Two', phrase: 'Number 2! Eyes 👀', speech: 'Number Two! Two bright eyes!', lang: 'en-US', icon: '👀' },
  '3': { word: 'Three', phrase: 'Number 3! Little Birds 🐣', speech: 'Number Three! Three little birds!', lang: 'en-US', icon: '🐣' },
  '4': { word: 'Four', phrase: 'Number 4! Wheels 🚗', speech: 'Number Four! Four fast wheels!', lang: 'en-US', icon: '🚗' },
  '5': { word: 'Five', phrase: 'Number 5! High Five ✋', speech: 'Number Five! Give me a high five!', lang: 'en-US', icon: '✋' }
};

// AI Voice Speech Synthesis for Popped Letters, Numbers & Devanagari Akshar
function speakBalloonCharacter(char) {
  if (!('speechSynthesis' in window) || !char) return;
  try {
    window.speechSynthesis.cancel(); // Stop pending speech

    const vocab = BALLOON_VOCABULARY[char] || {
      phrase: `${char}!`,
      speech: `${char}!`,
      lang: 'en-US',
      icon: '✨'
    };

    const utterance = new SpeechSynthesisUtterance(vocab.speech);
    utterance.lang = vocab.lang;
    utterance.rate = 0.95; // Gentle and clear for children
    utterance.pitch = 1.25; // Joyful, friendly voice
    utterance.volume = 1.0;

    // Search for clearest female or natural educational voice
    const voices = window.speechSynthesis.getVoices();
    if (voices && voices.length > 0) {
      const preferred = voices.find(v => (v.lang === vocab.lang || v.lang.startsWith(vocab.lang.slice(0, 2))) && (v.name.includes('Google') || v.name.includes('Natural') || v.name.includes('Female')));
      const fallback = voices.find(v => v.lang.startsWith(vocab.lang.slice(0, 2)));
      if (preferred) utterance.voice = preferred;
      else if (fallback) utterance.voice = fallback;
    }
    
    window.speechSynthesis.speak(utterance);
  } catch (e) {
    console.log('Speech synthesis:', e);
  }
}

function burstBalloon(balloonEl, event) {
  if (!balloonEl || balloonEl.classList.contains('bursting')) return;
  if (event) {
    event.stopPropagation();
    event.preventDefault();
  }

  // Trigger bursting state
  balloonEl.classList.add('bursting');

  // Trigger Instant Pop & Chime Audio
  playBalloonPopSound();

  const char = balloonEl.getAttribute('data-char') || '';
  const vocab = BALLOON_VOCABULARY[char] || {
    phrase: `${char}! Great job!`,
    speech: `${char}!`,
    lang: 'en-US',
    icon: '✨'
  };

  // Speak with friendly Montessori AI teacher voice
  if (char) {
    speakBalloonCharacter(char);
  }

  const rect = balloonEl.getBoundingClientRect();
  const container = document.getElementById('balloons-hero-layer') || document.body;
  const containerRect = container.getBoundingClientRect ? container.getBoundingClientRect() : { left: 0, top: 0 };
  
  const originX = rect.left - containerRect.left + rect.width / 2;
  const originY = rect.top - containerRect.top + rect.height / 2;

  // 1. Shockwave Ripple Ring
  const shockwave = document.createElement('div');
  shockwave.className = 'balloon-shockwave';
  shockwave.style.left = `${originX}px`;
  shockwave.style.top = `${originY}px`;
  container.appendChild(shockwave);
  setTimeout(() => shockwave.remove(), 600);

  // 2. Animated Talking Speech Bubble displaying the phonetic word & emoji
  const speechBubble = document.createElement('div');
  speechBubble.className = 'balloon-speech-bubble';
  speechBubble.style.left = `${originX}px`;
  speechBubble.style.top = `${originY - 10}px`;
  speechBubble.innerHTML = `
    <span class="bubble-icon">${vocab.icon}</span>
    <span class="bubble-char">${char}</span>
    <span class="bubble-phrase">${vocab.phrase}</span>
  `;
  container.appendChild(speechBubble);
  setTimeout(() => speechBubble.remove(), 1600);

  // 3. Generate 28 Vibrant Confetti Shards & Golden Sparkles
  const colors = ['#FF4081', '#00E676', '#FFD54F', '#00E5FF', '#7C4DFF', '#FF6E40', '#E040FB', '#FFD700'];
  for (let i = 0; i < 28; i++) {
    const spark = document.createElement('div');
    spark.className = 'balloon-pop-spark';
    const angle = (i / 28) * Math.PI * 2;
    const distance = 45 + Math.random() * 75;
    const dx = Math.cos(angle) * distance;
    const dy = Math.sin(angle) * distance;
    
    spark.style.setProperty('--dx', `${dx}px`);
    spark.style.setProperty('--dy', `${dy}px`);
    spark.style.left = `${originX}px`;
    spark.style.top = `${originY}px`;
    spark.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
    
    container.appendChild(spark);
    setTimeout(() => spark.remove(), 750);
  }

  // Hide the balloon after explosion animation
  setTimeout(() => {
    balloonEl.style.display = 'none';
  }, 340);

  // Respawn after 3.2 seconds with a fresh letter, number or Nepali akshar!
  setTimeout(() => {
    const alphabetSet = ['A', 'B', 'C', 'D', 'E', 'क', 'ख', 'ग', 'घ', 'ङ', '1', '2', '3', '4', '5'];
    const newChar = alphabetSet[Math.floor(Math.random() * alphabetSet.length)];
    balloonEl.setAttribute('data-char', newChar);
    const charSpan = balloonEl.querySelector('.balloon-char');
    if (charSpan) charSpan.textContent = newChar;
    balloonEl.classList.remove('bursting');
    balloonEl.style.display = 'flex';
  }, 3200);
}

// Push Notifications Request & Trigger Handler
async function requestAndShowNotification() {
  if (!('Notification' in window)) {
    alert('Your browser does not support desktop notifications.');
    return;
  }
  try {
    const permission = await Notification.requestPermission();
    if (permission === 'granted') {
      const response = await fetch('/api/push/test-notification/');
      const data = await response.json();
      
      new Notification(data.title, {
        body: data.body,
        icon: data.icon,
        badge: data.badge
      });

      const notifyBtns = [
        document.getElementById('enable-notifications-btn'),
        document.getElementById('footer-notify-trigger')
      ];
      notifyBtns.forEach(btn => {
        if (btn) {
          btn.innerHTML = '<i class="bi bi-bell-fill text-warning"></i>';
          btn.classList.add('active');
        }
      });
    } else {
      alert('Notifications were dismissed or blocked. You can re-enable them in browser site settings.');
    }
  } catch (err) {
    console.error('Notification error:', err);
  }
}

const notifyBtn = document.getElementById('enable-notifications-btn');
const footerNotifyBtn = document.getElementById('footer-notify-trigger');
if (notifyBtn) notifyBtn.addEventListener('click', requestAndShowNotification);
if (footerNotifyBtn) footerNotifyBtn.addEventListener('click', requestAndShowNotification);

// Dynamic AJAX Form Handlers with Toast Alerts
function setupAjaxForm(formId, resultContainerId) {
  const form = document.getElementById(formId);
  const resultContainer = document.getElementById(resultContainerId);
  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalBtnHtml = submitBtn ? submitBtn.innerHTML : '';
    
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status"></span>Submitting...';
    }

    const formData = new FormData(form);

    try {
      const res = await fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        }
      });
      const data = await res.json();

      if (data.success) {
        if (resultContainer) {
          resultContainer.innerHTML = `
            <div class="alert alert-success border-0 glass-panel p-3 mb-3 d-flex align-items-center gap-3">
              <i class="bi bi-check-circle-fill text-success fs-3"></i>
              <div>
                <strong class="d-block mb-1">Success!</strong>
                <span>${data.message}</span>
              </div>
            </div>
          `;
        }
        form.reset();
      } else {
        if (resultContainer) {
          resultContainer.innerHTML = `
            <div class="alert alert-danger border-0 glass-panel p-3 mb-3 d-flex align-items-center gap-3">
              <i class="bi bi-exclamation-triangle-fill text-danger fs-3"></i>
              <div>
                <strong class="d-block mb-1">Notice</strong>
                <span>${data.message}</span>
              </div>
            </div>
          `;
        }
      }
    } catch (err) {
      if (resultContainer) {
        resultContainer.innerHTML = `
          <div class="alert alert-danger border-0 glass-panel p-3 mb-3">
            An unexpected error occurred. Please try again.
          </div>
        `;
      }
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnHtml;
      }
    }
  });
}

// Scroll Navbar Blur
window.addEventListener('scroll', () => {
  const navbar = document.querySelector('.navbar-custom');
  if (navbar) {
    if (window.scrollY > 30) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }
});

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  setupAjaxForm('admission-inquiry-form', 'admission-form-response');
  setupAjaxForm('contact-inquiry-form', 'contact-form-response');

  const themeToggles = document.querySelectorAll('.theme-toggle-btn');
  themeToggles.forEach(btn => {
    btn.addEventListener('click', toggleTheme);
  });
});
