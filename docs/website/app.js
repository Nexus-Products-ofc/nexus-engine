async function boot() {
  const res = await fetch('locales.json');
  const data = await res.json();
  const select = document.getElementById('lang');
  const langs = data.languages || Object.keys(data.strings);
  const names = {
    en:'English', pt:'Português', es:'Español', fr:'Français', de:'Deutsch', it:'Italiano',
    ja:'日本語', zh:'中文', 'zh-tw':'繁體中文', ko:'한국어', ru:'Русский', ar:'العربية',
    hi:'हिन्दी', tr:'Türkçe', vi:'Tiếng Việt', id:'Indonesia', pl:'Polski', nl:'Nederlands',
    sv:'Svenska', uk:'Українська', th:'ไทย'
  };
  langs.forEach(code => {
    const opt = document.createElement('option');
    opt.value = code;
    opt.textContent = names[code] || code;
    select.appendChild(opt);
  });
  const saved = localStorage.getItem('nexus_lang') || navigator.language.slice(0,2) || data.default || 'en';
  const initial = data.strings[saved] ? saved : (data.default || 'en');
  select.value = initial;
  apply(data, initial);
  select.addEventListener('change', () => {
    localStorage.setItem('nexus_lang', select.value);
    apply(data, select.value);
    document.documentElement.lang = select.value;
    document.documentElement.dir = (select.value === 'ar' || select.value === 'he' || select.value === 'fa' || select.value === 'ur') ? 'rtl' : 'ltr';
  });
  document.documentElement.lang = initial;
}
function apply(data, code) {
  const table = data.strings[code] || data.strings.en || {};
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (table[key]) el.textContent = table[key];
  });
}
boot().catch(console.error);
