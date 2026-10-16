---
layout: default
title: Esomeprazole
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Esomeprazole：預測新適應症為十二指腸胃逆流 (Duodenogastric Reflux)（證據等級 L5）。原適應症：消化性潰瘍、胃食道逆流症、食道炎、Zollinger-Ellison 症候群等"
monitor_inn: "ESOMEPRAZOLE"
predicted_indications: ["duodenogastric reflux", "duodenal obstruction", "duodenal ulcer (disease)"]
---

# Esomeprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Esomeprazole：從消化性潰瘍／胃食道逆流到十二指腸胃逆流

## 一句話總結

Esomeprazole 是質子幫浦抑制劑，原本用於消化性潰瘍、胃食道逆流症與 Zollinger-Ellison 症候群等胃酸相關疾病。
TxGNN 模型預測它可能對**十二指腸胃逆流 (Duodenogastric Reflux)** 有效，但目前**沒有相關臨床試驗**，僅有 **1 篇**泛論質子幫浦抑制劑用途的文獻，證據相當薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 消化性潰瘍、胃食道逆流症、食道炎、Zollinger-Ellison 症候群等（來自知識圖譜；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 十二指腸胃逆流 (Duodenogastric Reflux) |
| TxGNN 預測分數 | 99.53% |
| 證據等級 | L5（僅有模型預測；唯一文獻為泛論性回顧，未直接討論此適應症） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張（皆為有效的單一成分許可證） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Esomeprazole 是質子幫浦抑制劑，透過抑制胃壁細胞的 H+/K+ ATPase 來抑制胃酸分泌，在胃酸相關疾病中的療效已被證實。

十二指腸胃逆流（膽汁逆流）的主因是十二指腸內容物（膽汁、胰液）逆流回胃，而不是胃酸過多。抑制胃酸或許能減輕胃與食道的黏膜傷害和症狀，但無法處理逆流本身，因此機轉上的關聯是**間接的**。

0.995 的高分只是計算預測，沒有試驗數據支持，不應單獨作為決策依據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | 質子幫浦抑制劑是消化性潰瘍、幽門螺旋桿菌感染、胃食道逆流症、NSAID 相關腸胃道損傷及 Zollinger-Ellison 症候群的首選藥物；未直接討論十二指腸胃逆流 |

---

## 香港上市資訊

共 20 張有效許可證，以下列出 5 張主要許可證。許可證資料未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-48058 | NEXIUM TAB 20MG（AstraZeneca） | 未載明 | 未載明 |
| HK-52131 | NEXIUM PDR FOR SOLN FOR INJ/INF 40MG（AstraZeneca） | 未載明（依品名為注射／輸注用粉劑） | 未載明 |
| HK-61717 | ESOMEPRAZOLE SANDOZ GASTRO-RESISTANT TABLETS 20MG | 未載明 | 未載明 |
| HK-64737 | EMANERA GASTRO-RESISTANT CAPSULES 40MG（Trenton-Boma） | 未載明 | 未載明 |
| HK-67261 | MAXEUM GASTRO-RESISTANT TABLETS 40MG（Julius Chen） | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜，非仿單內容）：肝衰竭、骨質疏鬆、停經後骨質疏鬆、骨折、慢性萎縮性胃炎。
- **藥物交互作用**：資料庫共記錄 100 筆交互作用，已取得的清單中，嚴重（Major）等級包括：
  - Acalabrutinib
  - Atazanavir

  中度（Moderate）等級包括：
  - Atorvastatin
  - Hydrochlorothiazide
  - Fenofibrate
  - Bendamustine
  - Bosutinib
  - Apalutamide
  - Amphotericin B
  - Amikacin

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 十二指腸胃逆流並非由胃酸驅動，Esomeprazole 的機轉只能間接緩解症狀，且沒有任何臨床試驗或直接文獻支持。
- 高預測分數僅為模型輸出，現階段不足以推進。

**若要推進需要：**
- 取得 Esomeprazole 的詳細作用機轉資料，並釐清其對膽汁逆流相關黏膜傷害的實際作用。
- 收集直接針對十二指腸胃逆流的臨床研究（例如質子幫浦抑制劑對膽汁逆流症狀或黏膜病變的研究）。
- 下載並解析香港衛生署的仿單，補齊警語與禁忌。

**補充觀察：** 同一份預測中排名第 3 的**十二指腸潰瘍**，有多項已完成的 Phase 3 試驗（例如 NCT00633932、NCT00633672、NCT00542789）和隨機對照文獻支持。它與原適應症「消化性潰瘍」高度重疊，屬於仿單內或接近仿單內的用途，不算真正的藥物再利用。若要選擇優先評估的方向，此項遠比十二指腸胃逆流合適，建議以 Proceed with Guardrails 另案評估：
- 確認各地區核准的適應症與劑量方案。
- 核對幽門螺旋桿菌的抗藥性資料。
- 留意多重藥物交互作用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

