---
layout: default
title: Cisatracurium
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cisatracurium：預測新適應症為馬尾症候群 (Cauda Equina Syndrome)（證據等級 L5）。原適應症：目前許可證資料未載明核准適應症"
monitor_inn: "Cisatracurium"
predicted_indications: ["cauda equina syndrome", "preeclampsia", "obsolete neurogenic bladder (disease)", "migraine disorder", "thrombotic disease", "irritable bowel syndrome", "migraine with brainstem aura", "mild pre-eclampsia", "severe pre-eclampsia", "neurocirculatory asthenia"]
---

# Cisatracurium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Cisatracurium：從神經肌肉阻斷（麻醉輔助）到 cauda equina syndrome（馬尾症候群）
{: .text-alpha }

## 一句話總結

Cisatracurium 是非去極化型神經肌肉阻斷劑，香港已有 11 張有效許可證。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 有效，但目前**沒有任何臨床試驗與直接相關文獻**，僅為模型預測，缺乏實證支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前許可證資料未載明核准適應症 |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的藥理分類，Cisatracurium 是作用於神經肌肉接合處菸鹼型乙醯膽鹼受體的非去極化型神經肌肉阻斷劑，臨床上用於麻醉時的肌肉鬆弛。

馬尾症候群是壓迫性神經急症，主要處置為手術減壓。神經肌肉阻斷作用無法處理其病因，**機轉上找不到合理的連結**。高分預測僅來自知識圖譜的關聯，不代表藥理上有效。

其他排名前十的預測（子癇前症、神經源性膀胱、偏頭痛、血栓性疾病、大腸急躁症等）同樣缺乏機轉依據與臨床證據。其中「神經源性膀胱」在疾病本體中已標示為過時術語，預測的有效性更受質疑。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測（馬尾症候群），目前無相關文獻。

作為參考，排名第 2 的子癇前症有兩篇間接文獻，但都是剖腹產麻醉管理的研究，Cisatracurium 至多是伴隨使用的麻醉藥，並非治療子癇前症的證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41103680](https://pubmed.ncbi.nlm.nih.gov/41103680/) | 2025 | 世代／比較研究 | Anesthesiology and Pain Medicine | 比較剖腹產全身麻醉與脊椎麻醉後的 IL-6、瘦體素、脂締素濃度，非 Cisatracurium 療效研究 |
| [18383970](https://pubmed.ncbi.nlm.nih.gov/18383970/) | 2008 | 病例系列 | Rev Esp Anestesiol Reanim | 12 例高風險剖腹產使用 remifentanil 單次注射控制血行動力 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66697 | CEMET SOLUTION FOR INJECTION/INFUSION 10MG/5ML | 注射液 | 資料未載明 |
| HK-65149 | CISATRACURIUM-HAMELN SOLUTION FOR INJECTION/INFUSION 10MG/5ML | 注射液 | 資料未載明 |
| HK-65681 | ACCORD CISATRACURIUM SOLUTION FOR INJECTION/INFUSION 20MG/10ML | 注射液 | 資料未載明 |
| HK-62323 | CISATRACURIUM NORMON SOLUTION FOR INJECTION AND FOR INFUSION 2MG/ML | 注射液 | 資料未載明 |
| HK-42333 | NIMBEX INJ 2MG/ML | 注射液 | 資料未載明 |

（共 11 張有效許可證，皆為單一成分，此處僅列 5 張。）

---

## 安全性考量

- **藥物交互作用**：共查得 61 筆交互作用，以下為部分主要項目：
  - **嚴重 (Major)**：Kanamycin、Neomycin、Paromomycin、Polymyxin B、Streptomycin（胺基糖苷類與多黏菌素可能增強神經肌肉阻斷）
  - **中度 (Moderate)**：Amphotericin B 各劑型、Doxycycline、Tetracycline、Minocycline、Vancomycin、Magnesium sulfate、Magnesium chloride、Mannitol、Metoclopramide
  - **輕微 (Minor)**：Ranitidine

特別提醒：子癇前症治療常用硫酸鎂，會增強神經肌肉阻斷劑的作用，使用時需特別留意。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症皆只有模型分數，沒有臨床試驗，也沒有直接支持療效的文獻，證據等級為 L5。
- Cisatracurium 的神經肌肉阻斷機轉與各預測疾病的病理機轉不吻合，且為靜脈注射、需監測環境使用，不適合長期治療用途。

**若要推進需要：**
- 補齊作用機轉與仿單的警語、禁忌症及原適應症資料
- 提出具體的藥理假說，說明神經肌肉阻斷如何作用於目標疾病
- 取得前臨床或臨床證據；在此之前，不建議投入進一步開發資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

