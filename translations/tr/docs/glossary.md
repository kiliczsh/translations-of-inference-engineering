# Çeviri Stil Kılavuzu ve Terim Sözlüğü
### *Inference Engineering* (Philip Kiely, Baseten Books) — Türkçe çeviri referansı

Bu belge, kitabın Türkçe çevirisinde **tutarlılığı** sağlamak için tek yetkili referanstır. Birden fazla çevirmen/ajan aynı kitabın farklı bölümlerini işlerken herkes buradaki kararlara uymalıdır. Bir terim burada bir karara bağlanmışsa, **alternatifi kullanılmaz** — "bağlama göre" veya "şu da olur" istisnaları tutarsızlık üretir.

> **Nasıl kullanılır:** Bir terimle karşılaşınca önce §4 alfabetik tabloya bak. Yoksa §1 karar mantığını uygula ve tabloya ekle. Türkçe ek/apostrof/sayı için §2'ye, üslup için §5'e bak.

---

## 1. Karar mantığı — çevir mi, İngilizce mi bırak?

Bir terimin İngilizce mi kalacağına yoksa çevrileceğine şu sırayla karar ver:

1. **Özel ad mı?** (ürün, kütüphane, marka, donanım kod adı, kısaltma) → **İngilizce kalır.** Örn. vLLM, CUDA, Hopper, LLM, KV cache.
2. **Türkçede yerleşik, yaygın ve doğal bir karşılığı var mı?** → **Çevrilir.** Örn. latency → gecikme, weights → ağırlıklar.
3. **Yerleşik ama teknik okuyucu İngilizcesini bekliyor mu?** (attention, transformer, pipeline, kernel, prompt, token) → **İngilizce kalır**, Türkçe ekle çekimlenir (token'lar, kernel'i).
4. **Çevrilebilir ama İngilizcesi kritik/aranan bir anahtar sözcük mü?** (quantization, embedding, disaggregation) → **Çevir + ilk geçişte parantezle İngilizcesini ver:** nicemleme (quantization).
5. Kararsız kaldığın her yeni terimi bu belgeye ekle ki bir sonraki çevirmen aynı kararı görsün.

**Altın kural:** Aynı kavram tüm kitapta **tek** karşılıkla anılır. İki seçenek arasında gidip gelme.

---

## 2. Türkçe biçim kuralları (hataların asıl kaynağı — dikkat)

### 2.1 Apostrof
- **Yalnızca düz apostrof** kullan: `'` (U+0027). Kıvrık `'` (U+2019) **kullanma.**
- İngilizce özel ad/kısaltma + Türkçe ek arasına apostrof: `GPU'ları`, `vLLM'i`, `token'lar`.
- **Sıradan Türkçe sözcüklere apostrof konmaz:** ~~önbellekleme'den~~ → **önbelleklemeden**, ~~nicemleme'yi~~ → **nicemlemeyi**.

### 2.2 Ünlü uyumlu ek (İngilizce sözcüklerde)
Ek, sözcüğün **Türkçe okunuşundaki son ünlüye** göre seçilir:
| Sözcük | Okunuş (son ünlü) | Doğru | Yanlış |
|---|---|---|---|
| token | "tokın" (art) | token'**lar**, token'**ı**, token'**lara** | ~~token'ler~~, ~~token'leri~~ |
| kernel | "körnıl" (art) | kernel'**lar**, kernel'**ı** | — |
| GPU | "ci-pi-**yu**" (art) | GPU'**lar**, GPU'**ya**, GPU'**da** | — |
| CPU | "si-pi-**yu**" (art) | CPU'**lar**, CPU'**ya** | — |
| LLM | "el-el-**em**" (ön) | LLM'**ler**, LLM'**ye**, LLM'**de** | ~~LLM'lar~~ |
| API | "ey-pi-**ay**" (ön) | API'**ler**, API'**ye** | — |
| vLLM | "vi-el-el-**em**" (ön) | vLLM'**i**, vLLM'**ye** | — |

### 2.3 Kısaltmalarda yönelme/belirtme eki
Son sese göre: **LLM'ye**, **API'ye**, **GPU'ya**, **VLM'ye**, **CPU'ya**. (LLM'e/VLM'e değil.)

### 2.4 Çoğul
Türkçe çoğul eki tercih edilir: **expert'ler**, **token'lar**, **kernel'lar** — İngilizce `-s` ile değil (~~experts~~, ~~tokens~~).

### 2.5 Sayılar ve birimler
- Ondalık ayırıcı: **virgül** (5,3 petaFLOPS; %99,99). Binlik: nokta veya boşluk.
- Model/sürüm/donanım adlarındaki sayılar **aynen** korunur (GPT-5, Llama 3, B200, FP8, 5P3D).
- Yüzde işareti sayıdan önce, bitişik: **%20** (yüzde de yazılabilir: "yüzde 20").

### 2.6 Parantezli İngilizce kuralı
- Çevrilen anahtar terimin İngilizcesi, **her bölümde ilk geçtiği yerde** parantezle verilir: "nicemleme (quantization)". Aynı bölüm içinde tekrarlanmaz. (Bölümler bağımsız okunabildiği için her bölüm kendi ilk geçişini alır.)

### 2.7 Asla çevrilmeyecekler
Kod blokları, komutlar, dosya/yol adları, matematiksel formüller ve denklemler, figür/tablo **numaraları** (1.1, 2.3), URL'ler, akademik atıflar (makale başlıkları, yazar adları, dergi adları) — hepsi **aynen** kalır. Yalnızca çevresindeki açıklama metni çevrilir.

### 2.8 İngilizce teknik terimler italik
- İngilizce kalan tüm teknik terimler (ortak sözcükler, kısaltmalar, ürün/model/mimari adları) gövde metninde **italik** yazılır: `<i>token</i>`, `<i>LLM</i>`, `<i>KV cache</i>`, `<i>vLLM</i>`.
- Yalnızca terim kökü italik olur; **Türkçe ek düz kalır:** `<i>token</i>'ları`, `<i>GPU</i>'da`.
- Zaten italik olan bağlamlar (kitap/makale başlıkları) **tekrar sarılmaz** (iç içe `<i>` yok).

### 2.9 Metin hizalaması
- Normal paragraflar: **iki yana yaslı** (`text-align: justify`).
- Liste öğeleri (`<li>` / `.liste_txt_courant_ssalinea`): **sola yaslı** (`text-align: left`).

---

## 3. İngilizce kalacak kategoriler (çevrilmez)

- **Ürün / kütüphane / marka:** vLLM, SGLang, TensorRT-LLM, TensorRT, ONNX Runtime, PyTorch, CUDA, cuDNN, cuBLAS, CUTLASS, NVIDIA Dynamo, Triton, Baseten, Hugging Face, Docker, Kubernetes, PyPI, Whisper, DeepSeek, Llama, Qwen, Kimi, GPT, Gemini, Claude, NIM, FlashAttention, ComfyUI, SDXL
- **Donanım / mimari kod adları:** Hopper, Ada Lovelace, Blackwell, Rubin, Feynman, Ampere, Grace, Vera, H100, H200, B200, B300, GB200, GH200, NVL72, NVLink, NVSwitch, InfiniBand, HBM3e, SXM, PCIe
- **Kısaltmalar:** LLM, VLM, ASR, TTS, GPU, CPU, API, TTFT, TPS, ITL, KV cache, MoE, RAG, SLA, SLO, RTF, VAD, ISL, OSL, OOM, MIG, TP, EP, PP, CP, LoRA, GEMM, BLAS, SM, VRAM, FP8/FP4/BF16, MMLU, SWE-bench, Elo, P50/P90/P95/P99
- **Yerleşik teknik sözcükler** (Türkçe ekle çekimlenir): attention, transformer, token, batch, prefill, decode, cache (KV cache içinde), checkpoint, kernel, prompt, pipeline, softmax, logit, roofline, prefix, runtime, temperature, top-k, top-p, serving (disaggregated serving), fine-tuning, embedding
- **Not:** Kitap başlığı kapak/künyede İngilizce kalır ("Inference Engineering"); iç metinde ilk geçişte "Çıkarım Mühendisliği (Inference Engineering)" verilebilir.

---

## 4. Alfabetik terim tablosu (tek karşılık — bağlayıcı)

| İngilizce | Türkçe karşılık | Not |
|---|---|---|
| all-to-all | tümü-tümüne (all-to-all) | ~~hepten-hepe~~ değil |
| arithmetic intensity | aritmetik yoğunluk | |
| autoscaling | otomatik ölçekleme | |
| cache (KV cache) | *(İngilizce)* KV cache | |
| cache (genel, isim) | önbellek | |
| cache-aware | önbellek farkındalıklı | ~~önbellek duyarlı~~ değil (topoloji/coğrafi farkındalıklı ile uyumlu) |
| caching | önbellekleme | |
| cold start | soğuk başlangıç (cold start) | |
| containerization | konteynerleştirme | |
| context window | bağlam penceresi | ~~context window~~ İngilizce bırakma |
| cost-effective | uygun maliyetli | ~~maliyet etkin~~ değil |
| deployment | dağıtım | ~~deployment~~ İngilizce bırakma; "dedicated deployment" → özel dağıtım |
| diffusion | difüzyon | ~~diffusion~~ İngilizce bırakma (ürün adı "SGLang Diffusion" hariç) |
| disaggregation | disaggregation (ayrıştırma) | terim İngilizce kalır, ilk geçişte parantez |
| distillation | damıtma | |
| embedding | *(İngilizce)* embedding | ~~gömme~~ değil (fiil 'gömülmek/gömmek' Türkçe kalabilir) | |
| evals / evaluation | değerlendirme (eval) | |
| fine-tuning | *(İngilizce)* fine-tuning | fiil: fine-tuning yapmak; sıfat: fine-tune edilmiş; ~~ince ayar~~ değil | |
| foundation model | temel model | |
| generative | üretken | ~~üretici~~ değil (üretici = manufacturer/generator, farklı anlam) |
| inference | çıkarım | |
| inference engine | çıkarım motoru | ~~çıkarım engine~~ değil |
| inference engineering | çıkarım mühendisliği | |
| kernel fusion | kernel füzyonu | |
| latency | gecikme | |
| load balancing | yük dengeleme | |
| local / edge inference | yerel / kenar çıkarım | tutarlı kullan; "edge" → kenar |
| model parallelism | model paralelliği | Tensor/Expert/Pipeline/Context Paralelliği |
| neural network | sinir ağı | |
| offline / online inference | çevrimdışı / çevrimiçi çıkarım | |
| production (environment) | canlı ortam | ~~prodüksiyon~~ / ~~üretim ortamı~~ değil; "in production" → "canlı ortamda", "go to production" → "canlıya almak", "Chapter 7: Production" → "Bölüm 7: Canlı Ortam" |
| quantization | nicemleme (quantization) | |
| reasoning | akıl yürütme | |
| reliability | güvenilirlik | |
| routing | yönlendirme | |
| runtime | *(İngilizce)* runtime | Türkçe ekle çekimlenir (runtime'da, runtime'ı); ~~çalışma zamanı~~ kullanma. Ürün adı "ONNX Runtime" büyük R |
| temperature | *(İngilizce)* temperature | örnekleme parametresi, İngilizce kalır (top-k/top-p ile uyumlu); ~~sıcaklık~~ kullanma |
| scaling | ölçekleme | |
| shared / dedicated inference | paylaşımlı / özel çıkarım | |
| speculation | spekülasyon | |
| speculative decoding | spekülatif decoding | decode/decoding İngilizce kalır |
| throughput | verim | ~~aktarım hızı~~ değil (tek karşılık: verim) |
| tradeoff | ödünleşim | |
| vocabulary | sözlük | ~~kelime dağarcığı~~ değil |
| weights | ağırlıklar | model weights → model ağırlıkları |
| workload | iş yükü | çoğul: iş yükleri |

---

## 5. Üslup

- **Akıcı, doğal teknik kitap Türkçesi.** Kelime kelime değil; anlamı koru. Uzun İngilizce cümleleri gerektiğinde **böl** — devrik/hantal "çeviri kokan" cümlelerden kaçın.
- **Hitap:** "siz" (resmi ama samimi teknik kitap tonu).
- **Analojiler** (NFL, sumo, olimpik sporcu vb.) doğal Türkçeye uyarlanır; kültürel referans Türk okuyucu için anlaşılırsa korunur.
- **Deyimlerde birebir çeviriden kaçın:** "under the hood" → "iç işleyiş" (~~kaputun altında~~ zorunlu değil), "out of the box" → "hazır haliyle", "sharp edges" → "beklenmedik tuzaklar" (~~sivri uçlar~~ değil).
- **Numaralandırma:** başlık (1.1, 1.2.1) ve figür/tablo numaraları **aynen** korunur. Bölüm gövdesindeki başlıklar ile İçindekiler/nav **birebir** aynı olmalı.
- **Tutarlılık kontrolü:** Bir bölümü bitirince §4 tablosundaki terimleri metinde tara; İngilizce kalıntı (parallelism, caching, engine, deployment) ve alternatif karşılık (aktarım hızı, üretim ortamı, maliyet etkin) bırakma.

---

## 6. Sık yapılan hatalar (kontrol listesi)

- [ ] Kıvrık apostrof (`'`) → düz (`'`) yapıldı mı?
- [ ] `token'lar` (art ünlü), `LLM'ler`/`LLM'ye` (ön ünlü) doğru mu?
- [ ] `throughput` her yerde **verim** mi? (aktarım hızı sızmış mı?)
- [ ] `production` her yerde **canlı ortam** mı? (~~prodüksiyon~~ kalmış mı?)
- [ ] `inference engine` → **çıkarım motoru** mu? ("engine" kalmış mı?)
- [ ] `generative` → **üretken** mi? (üretici = manufacturer, karıştırma)
- [ ] `caching/parallelism/deployment` gövdede İngilizce kalmış mı?
- [ ] Başlıklar İçindekiler/nav.xhtml/toc.ncx ile birebir aynı mı?
- [ ] Figür/tablo numaraları ve `<img src>` yolları korundu mu?
