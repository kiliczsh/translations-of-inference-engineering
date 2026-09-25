#!/usr/bin/env python3
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "src" / "epub" / "OPS"

# same keys as before but matching is now whitespace/nbsp-insensitive
MAP = {
    "1.1 Scale and Specialization": "1.1 Ölçek ve Uzmanlaşma",
    "1.2 About Your App": "1.2 Uygulamanız Hakkında",
    "1.2.1 AI-Native Applications": "1.2.1 Yapay Zeka Yerleşik Uygulamalar",
    "1.2.2 Online versus Offline": "1.2.2 Çevrimiçi ve Çevrimdışı",
    "1.2.3 Consumer versus B2B": "1.2.3 Tüketici ve B2B",
    "1.3 Model Selection": "1.3 Model Seçimi",
    "1.3.1 Model Evaluation": "1.3.1 Model Değerlendirmesi",
    "1.3.2 Fine-Tuning for Domain-Specific Quality": "1.3.2 Alana Özgü Kalite için İnce Ayar",
    "1.3.3 Distillation": "1.3.3 Damıtma",
    "1.4 Measuring Latency and Throughput": "1.4 Gecikme ve Verimi Ölçmek",
    "1.4.1 Latency Percentiles": "1.4.1 Gecikme Yüzdelikleri",
    "1.4.2 End-to-End Metrics": "1.4.2 Uçtan Uca Metrikler",
    "2.1 Neural Networks": "2.1 Sinir Ağları",
    "2.1.1 Linear Layers and Matmul": "2.1.1 Doğrusal Katmanlar ve Matmul",
    "2.1.2 Activation Functions": "2.1.2 Aktivasyon Fonksiyonları",
    "2.2 LLM Inference Mechanics": "2.2 LLM Çıkarım Mekanikleri",
    "2.2.1 LLM Architecture": "2.2.1 LLM Mimarisi",
    "2.2.2 Transformer Blocks": "2.2.2 Transformer Blokları",
    "2.2.3 Attention": "2.2.3 Attention",
    "2.2.4 Mixture of Experts Models": "2.2.4 Mixture of Experts (Uzman Karışımı) Modelleri",
    "2.3 Image Generation Inference Mechanics": "2.3 Görsel Üretimi Çıkarım Mekanikleri",
    "2.3.1 Image Generation Model Architecture": "2.3.1 Görsel Üretim Model Mimarisi",
    "2.3.2 Few-Step Image Generation Models": "2.3.2 Az Adımlı Görsel Üretim Modelleri",
    "2.3.3 Video Generation": "2.3.3 Video Üretimi",
    "2.4 Calculating Inference Bottlenecks": "2.4 Çıkarım Darboğazlarını Hesaplamak",
    "2.4.1 Ops:Byte Ratio and Arithmetic Intensity": "2.4.1 Ops:Byte Oranı ve Aritmetik Yoğunluk",
    "2.4.2 LLM Inference Bottlenecks": "2.4.2 LLM Çıkarım Darboğazları",
    "2.4.3 Image Generation Inference Bottlenecks": "2.4.3 Görsel Üretimi Çıkarım Darboğazları",
    "2.5 Optimizing Attention": "2.5 Attention'ı Optimize Etmek",
    "3.1 GPU Architecture": "3.1 GPU Mimarisi",
    "3.1.1 Compute": "3.1.1 İşlem Gücü",
    "3.1.2 Memory and Caches": "3.1.2 Bellek ve Önbellekler",
    "3.2 GPU Architecture Generations": "3.2 GPU Mimari Nesilleri",
    "3.2.1 Hopper GPUs": "3.2.1 Hopper GPU'ları",
    "3.2.2 Ada Lovelace GPUs": "3.2.2 Ada Lovelace GPU'ları",
    "3.2.3 Blackwell GPUs": "3.2.3 Blackwell GPU'ları",
    "3.2.4 Rubin GPUs": "3.2.4 Rubin GPU'ları",
    "3.2.5 Grace and Vera CPUs": "3.2.5 Grace ve Vera CPU'ları",
    "3.3 Instances": "3.3 Instance'lar",
    "3.3.1 Multi-GPU Instances": "3.3.1 Çoklu GPU Instance'ları",
    "3.3.2 Multi-Instance GPUs": "3.3.2 Çoklu Instance GPU'lar (MIG)",
    "3.4 Other Datacenter Accelerator Options": "3.4 Diğer Veri Merkezi Hızlandırıcı Seçenekleri",
    "3.5 Local Inference": "3.5 Lokal Çıkarım",
    "3.5.1 Desktop Inference": "3.5.1 Masaüstü Çıkarım",
    "3.5.2 Mobile Inference": "3.5.2 Mobil Çıkarım",
    "4.1 CUDA": "4.1 CUDA",
    "4.1.1 CUDA Kernels for Inference": "4.1.1 Çıkarım için CUDA Kernel'leri",
    "4.1.2 CUDA Kernel Selection": "4.1.2 CUDA Kernel Seçimi",
    "4.1.3 Reducing Memory Accesses with Kernel Fusion": "4.1.3 Kernel Füzyonu ile Bellek Erişimlerini Azaltmak",
    "4.2 Deep Learning Frameworks and Libraries": "4.2 Derin Öğrenme Çerçeveleri ve Kütüphaneleri",
    "4.2.1 PyTorch": "4.2.1 PyTorch",
    "4.2.2 Model File Formats": "4.2.2 Model Dosya Formatları",
    "4.2.3 ONNX Runtime and TensorRT": "4.2.3 ONNX Runtime ve TensorRT",
    "4.2.4 Transformers and Diffusers": "4.2.4 Transformers ve Diffusers",
    "4.3 Inference Engines": "4.3 Çıkarım Motorları",
    "4.3.1 vLLM": "4.3.1 vLLM",
    "4.3.2 SGLang": "4.3.2 SGLang",
    "4.3.3 TensorRT-LLM": "4.3.3 TensorRT-LLM",
    "4.4 NVIDIA Dynamo": "4.4 NVIDIA Dynamo",
    "4.5 Performance Benchmarking and Load Testing": "4.5 Performans Karşılaştırması ve Yük Testi",
    "4.5.1 Performance Benchmarking Tooling": "4.5.1 Performans Karşılaştırma Araçları",
    "4.5.2 Performance Benchmarking Tips": "4.5.2 Performans Karşılaştırma İpuçları",
    "4.5.3 Profiling Performance": "4.5.3 Performans Profilleme",
    "5.1 Quantization": "5.1 Nicemleme (Quantization)",
    "5.1.1 Number Formats": "5.1.1 Sayı Formatları",
    "5.1.2 Quantization Approaches": "5.1.2 Nicemleme Yaklaşımları",
    "5.1.3 Measuring Quality Impact": "5.1.3 Kalite Etkisini Ölçmek",
    "5.2 Speculative Decoding": "5.2 Spekülatif Decoding",
    "5.2.1 Draft-Target Speculative Decoding": "5.2.1 Draft-Target Spekülatif Decoding",
    "5.2.2 Medusa": "5.2.2 Medusa",
    "5.2.3 EAGLE": "5.2.3 EAGLE",
    "5.2.4 N-gram Speculation and Lookahead Decoding": "5.2.4 N-gram Spekülasyonu ve Lookahead Decoding",
    "5.3 Caching": "5.3 Önbellekleme",
    "5.3.1 Prefix Caching and KV Cache Re-Use": "5.3.1 Prefix Önbellekleme ve KV Cache Yeniden Kullanımı",
    "5.3.2 Where to Store the KV Cache": "5.3.2 KV Cache Nerede Saklanır",
    "5.3.3 Cache-Aware Routing": "5.3.3 Önbellek Duyarlı Yönlendirme",
    "5.3.4 Long Context Handling": "5.3.4 Uzun Bağlam Yönetimi",
    "5.4 Model Parallelism": "5.4 Model Paralelliği",
    "5.4.1 Tensor Parallelism for Lower Latency": "5.4.1 Daha Düşük Gecikme için Tensor Paralelliği",
    "5.4.2 Expert Parallelism for Higher Throughput": "5.4.2 Daha Yüksek Verim için Expert Paralelliği",
    "5.4.3 Multi-Node Inference": "5.4.3 Çoklu Node Çıkarımı",
    "5.5 Disaggregation": "5.5 Disaggregation (Ayrıştırma)",
    "5.5.1 How Disaggregation Works": "5.5.1 Disaggregation Nasıl Çalışır",
    "5.5.2 When to Use Disaggregation": "5.5.2 Disaggregation Ne Zaman Kullanılır",
    "5.5.3 Dynamic Disaggregation with NVIDIA Dynamo": "5.5.3 NVIDIA Dynamo ile Dinamik Disaggregation",
    "6.1 Vision Language Models": "6.1 Görsel Dil Modelleri (VLM)",
    "6.1.1 Video Processing for Vision Language Models": "6.1.1 Görsel Dil Modelleri için Video İşleme",
    "6.1.2 Omni-Modal Models": "6.1.2 Omni-Modal Modeller",
    "6.2 Embedding Models": "6.2 Gömme (Embedding) Modelleri",
    "6.2.1 Embedding Model Architecture": "6.2.1 Embedding Model Mimarisi",
    "6.2.2 Embedding Model Inference": "6.2.2 Embedding Model Çıkarımı",
    "6.3 ASR Models": "6.3 ASR Modelleri",
    "6.3.1 Single-Chunk Latency Optimization": "6.3.1 Tek Parça Gecikme Optimizasyonu",
    "6.3.2 Long File Latency Optimization": "6.3.2 Uzun Dosya Gecikme Optimizasyonu",
    "6.3.3 Diarization": "6.3.3 Diarization (Konuşmacı Ayrıştırma)",
    "6.4 TTS Models": "6.4 TTS Modelleri",
    "6.4.1 Streaming Real-Time Text to Speech": "6.4.1 Gerçek Zamanlı Akışlı Metinden Sese",
    "6.4.2 Speech-to-Speech Models": "6.4.2 Sesten Sese Modeller",
    "6.5 Image Generation Models": "6.5 Görsel Üretim Modelleri",
    "6.5.1 Image Generation Kernel Optimization": "6.5.1 Görsel Üretimi Kernel Optimizasyonu",
    "6.5.2 One Weird Trick for Faster Image Generation": "6.5.2 Daha Hızlı Görsel Üretimi için Tuhaf Bir Numara",
    "6.6 Video Generation Models": "6.6 Video Üretim Modelleri",
    "6.6.1 Attention Optimization and Quantization": "6.6.1 Attention Optimizasyonu ve Nicemleme",
    "6.6.2 Context Parallelism": "6.6.2 Context Paralelliği",
    "7.1 Containerization": "7.1 Konteynerleştirme",
    "7.1.1 Dependency Management": "7.1.1 Bağımlılık Yönetimi",
    "7.1.2 NIMs": "7.1.2 NIM'ler",
    "7.2 Autoscaling": "7.2 Otomatik Ölçekleme",
    "7.2.1 Concurrency and Batch Sizing": "7.2.1 Eşzamanlılık ve Batch Boyutlandırma",
    "7.2.2 Cold Starts": "7.2.2 Soğuk Başlangıçlar",
    "7.2.3 Routing, Load Balancing, and Queueing": "7.2.3 Yönlendirme, Yük Dengeleme ve Kuyruklama",
    "7.2.4 Scale to Zero": "7.2.4 Sıfıra Ölçekleme",
    "7.2.5 Independent Component Scaling": "7.2.5 Bağımsız Bileşen Ölçekleme",
    "7.3 Multi-Cloud Capacity Management": "7.3 Çoklu Bulut Kapasite Yönetimi",
    "7.3.1 GPU Procurement": "7.3.1 GPU Tedariki",
    "7.3.2 Geo-Aware Load Balancing": "7.3.2 Coğrafi Duyarlı Yük Dengeleme",
    "7.3.3 Building for Reliability": "7.3.3 Güvenilirlik için Tasarım",
    "7.3.4 Security and Compliance": "7.3.4 Güvenlik ve Uyumluluk",
    "7.4 Testing and Deployment": "7.4 Test ve Dağıtım",
    "7.4.1 Zero-Downtime Deployment": "7.4.1 Kesintisiz Dağıtım",
    "7.4.2 Cost Estimation": "7.4.2 Maliyet Tahmini",
    "7.4.3 Observability": "7.4.3 Gözlemlenebilirlik",
    "7.5 Client Code": "7.5 İstemci Kodu",
    "7.5.1 Client Latency Overhead": "7.5.1 İstemci Gecikme Yükü",
    "7.5.2 Asynchronous inference": "7.5.2 Asenkron çıkarım",
    "7.5.3 Streaming and Protocol Support": "7.5.3 Akış ve Protokol Desteği",
    "7.6 Production Inference with Baseten": "7.6 Baseten ile Prodüksiyon Çıkarımı",
}

FILES = ["nav.xhtml", "sommaire.xhtml", "toc.ncx"]

total_subs = 0
for fname in FILES:
    path = f"{BASE}/{fname}"
    with open(path, encoding="utf-8") as f:
        content = f.read()
    subs_here = 0
    for key in sorted(MAP, key=len, reverse=True):
        # build a flexible regex: any run of whitespace/nbsp in key becomes [\s\xa0]+
        pattern = re.escape(key)
        pattern = pattern.replace(r"\ ", r"[\s\xa0]+")
        full_pattern = ">(" + pattern + ")<"
        new_content, n = re.subn(full_pattern, f">{MAP[key]}<", content)
        if n:
            content = new_content
            subs_here += n
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{fname}: {subs_here} headings translated")
    total_subs += subs_here

print("total:", total_subs)
