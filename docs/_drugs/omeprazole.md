---
layout: default
title: Omeprazole
parent: 中證據等級 (L3-L4)
nav_order: 645
evidence_level: L3
indication_count: 2
---

# Omeprazole
{: .fs-9 }

證據等級: **L3** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Omeprazole：從消化性潰瘍與胃食道逆流到十二指腸胃逆流

## 一句話總結

Omeprazole 是質子幫浦抑制劑，原本用於胃潰瘍、十二指腸潰瘍、胃食道逆流症與 Zollinger-Ellison 症候群等酸相關疾病。
TxGNN 模型預測它可能對**十二指腸胃逆流 (Duodenogastric Reflux)** 有效，但目前僅有 **1 個間接相關的臨床試驗**和 **15 篇文獻**（多為動物或小型機轉研究），證據仍屬初步。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃潰瘍、消化性潰瘍、胃食道逆流症、食道炎、十二指腸潰瘍、Zollinger-Ellison 症候群（來自知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 十二指腸胃逆流 (Duodenogastric Reflux) |
| TxGNN 預測分數 | 99.64% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Omeprazole 是質子幫浦抑制劑，能抑制胃酸分泌，並已用於胃食道逆流症、食道炎與消化性潰瘍。這些疾病與十二指腸胃逆流（膽汁與十二指腸內容物逆流入胃）在病理上有部分重疊，因此模型給出高分。

酸抑制可能減輕酸與膽汁混合逆流造成的黏膜傷害與症狀，但 **Omeprazole 並不會減少膽汁逆流本身**。

需要特別注意的是，大鼠研究（PMID 10389684、8943968、33027361）顯示，在十二指腸胃逆流的情況下合併胃酸阻斷，可能促進前腸黏膜增生與胃部致癌，這是需要釐清的安全性訊號。人體資料目前僅限於 Barrett 食道的小型機轉研究（PMID 10994616、9824338）與一項兒童食道膽汁逆流的前瞻性研究（PMID 16641575）。0.996 的預測分數與既有逆流適應症的重疊相符，但終究只是模型預測。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | 不適用 | 完成 | 157 | 以內視鏡三模影像區分功能性消化不良與逆流疾病，屬診斷研究，並未測試 Omeprazole，僅有背景參考價值 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | PPI 臨床使用與藥動學更新，為消化性潰瘍、胃食道逆流症等的首選藥物 |
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | 人體機轉研究 | Scand J Gastroenterol | 探討 Omeprazole 對 Barrett 食道患者胃竇十二指腸胃逆流的影響 |
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | 人體機轉研究 | Gut | 每日兩次 20 mg Omeprazole 對 Barrett 食道的十二指腸胃逆流與胃食道膽汁逆流的影響 |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | 前瞻性研究（兒童） | J Pediatr Gastroenterol Nutr | 以 PPI 治療兒童食道膽汁逆流的前瞻性研究 |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | 描述性臨床研究 | Eur J Pediatr | 6 名兒童與青少年原發性十二指腸胃逆流，對傳統制酸治療反應不佳 |
| [8076761](https://pubmed.ncbi.nlm.nih.gov/8076761/) | 1994 | 生理學研究 | Gastroenterology | 探討 pH、十二指腸胃食道逆流與 Barrett 食道的關係 |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | 動物研究（大鼠） | Dig Dis Sci | 胃酸阻斷會促進十二指腸胃逆流誘發的胃部致癌 |
| [8943968](https://pubmed.ncbi.nlm.nih.gov/8943968/) | 1996 | 動物研究（大鼠） | Dig Dis Sci | 十二指腸胃逆流造成前腸黏膜增生，胃酸阻斷會加劇此效應 |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | 動物研究（大鼠） | Acta Cir Bras | 探討 Omeprazole 對十二指腸胃逆流大鼠胃腺癌是否具保護作用 |
| [20697939](https://pubmed.ncbi.nlm.nih.gov/20697939/) | 2010 | 臨床研究（針灸，間接） | Chin J Integr Med | 針灸治療胃食道逆流的療效與安全性，與 Omeprazole 無直接關係 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67684 | OMEPRAZOLE JEAN-MARIE GASTRO-RESISTANT CAPSULES 20MG | 膠囊（耐胃酸） | 未提供 |
| HK-53339 | OMEDIN 20 CAP 20MG (ENTERIC COATED PELLETS) | 膠囊（腸溶顆粒） | 未提供 |
| HK-49774 | GOMEC CAP 20MG (E.C. GRANULES) | 膠囊（腸溶顆粒） | 未提供 |
| HK-44354 | LOSEC MUPS TAB 20MG | 錠劑 | 未提供 |
| HK-44353 | LOSEC MUPS TAB 10MG | 錠劑 | 未提供 |

香港共有 20 張有效的單方許可證，目前沒有已註銷者；以上僅列出 5 張。

---

## 安全性考量

- **知識圖譜中的禁忌關聯疾病**（非仿單內容）：肝衰竭、肝臟疾病、膽囊疾病、充血性心臟衰竭、骨質疏鬆、停經後骨質疏鬆、骨折、慢性萎縮性胃炎。
- **藥物交互作用**：資料庫共記錄 100 筆，以下為其中較重要者：
  - 重度：Acalabrutinib、Atazanavir
  - 中度：Alprazolam、Amphotericin B、Amikacin、Amphetamine、Apalutamide、Armodafinil、Atorvastatin、Fenofibrate、Hydrochlorothiazide 等
  - 輕度：Lidocaine、Nifedipine、Ambrisentan、Acetylsalicylic acid
- **動物研究訊號**：大鼠模型中，十二指腸胃逆流合併胃酸阻斷可能促進黏膜增生與胃部致癌，尚未在人體證實。

仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一的臨床試驗是診斷影像研究，並未測試 Omeprazole；文獻多為動物或小型機轉研究，且沒有任何針對十二指腸胃逆流的對照試驗。
- Omeprazole 不降低膽汁逆流，且動物資料提示酸阻斷可能增加致癌風險，在釐清前不宜推進。

**若要推進需要：**
- 取得香港仿單的警語與禁忌資料，完成安全性篩選
- 取得詳細的作用機轉資料
- 針對十二指腸胃逆流族群設計隨機對照試驗，並以膽汁逆流指標與症狀為終點
- 釐清酸抑制合併膽汁逆流的長期致癌與黏膜增生風險，必要時納入內視鏡追蹤
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

