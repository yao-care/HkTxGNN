---
layout: default
title: Ambroxol
parent: 中證據等級 (L3-L4)
nav_order: 48
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Ambroxol：預測新適應症為鼻腔疾病 (Nasal Cavity Disease)（證據等級 L4）。原適應症：咽炎 (Pharyngitis)"
monitor_inn: "Ambroxol"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "vulvovaginal candidiasis", "faucial diphtheria", "cervical disc degenerative disorder"]
---

# Ambroxol
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

## Ambroxol：從咽炎到鼻腔疾病
{: .text-alpha }

## 一句話總結

Ambroxol 是一種黏液溶解／袪痰藥物，原本用於咽炎（pharyngitis）。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇間接相關文獻**（急性咳嗽的綜述），證據仍屬早期。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 咽炎 (Pharyngitis) |
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，Ambroxol 是黏液溶解／分泌促進劑，可促進黏液纖毛清除並降低黏液黏稠度。另有報告指出它具有類局部麻醉（鈉通道阻斷）與抗發炎特性。

咽炎與鼻腔疾病同屬上呼吸道疾病，常伴隨黏液分泌異常，因此從機轉上看，改善黏液清除可能對鼻腔疾病有幫助。不過，這僅是間接推論，目前沒有針對鼻腔疾病的直接臨床證據。

此外，Ambroxol 作用於 GBA1（glucosylceramidase beta）的伴護蛋白（chaperone）活性，正被探索用於神經退化性疾病，但與鼻腔疾病無明確關聯。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26525480](https://pubmed.ncbi.nlm.nih.gov/26525480/) | 2015 | Review | Vestnik otorinolaringologii | 探討流感與急性呼吸道病毒感染相關急性咳嗽的治療新選擇；屬間接證據，未直接針對鼻腔疾病 |

## 香港上市資訊

本藥在香港共有 20 張有效的單一成分許可證，以下列出 5 張主要許可證（資料中未載明劑型與核准適應症）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55459 | OBROXOL ORAL SOLUTION 30MG/10ML | 口服液 | 資料未載明 |
| HK-34878 | AMXOL TAB 30MG | 錠劑 | 資料未載明 |
| HK-61486 | UNION AMBROXOL TAB 30MG | 錠劑 | 資料未載明 |
| HK-46048 | AMBROXOL TAB 30MG | 錠劑 | 資料未載明 |
| HK-44882 | AMBROXOL SR CAP 75MG (BRIGHT FUTURE) | 緩釋膠囊 | 資料未載明 |

## 安全性考量

- **藥物交互作用**：資料庫查詢到 1 筆藥理學層面的交互作用，對象為 glucosylceramidase beta (GBA1)。Ambroxol 在細胞內（酸性溶酶體環境）可提高 GCase 酵素活性，在無細胞、中性 pH 環境下則呈抑制作用。此為藥理標靶資訊，未標示臨床嚴重程度。

其餘警語與禁忌症資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 預測分數很高（99.91%），但沒有任何針對鼻腔疾病的臨床試驗，唯一文獻也只是急性咳嗽的間接綜述，證據等級僅 L4。
- 作用機轉只是合理推測，且缺乏仿單的警語與禁忌症資料，尚無法進行安全性篩選。

**若要推進需要：**
- 取得 Ambroxol 完整的作用機轉資料（MOA）
- 下載並解析香港衛生署的仿單，確認警語、禁忌症與核准適應症
- 針對鼻腔疾病（如鼻竇炎、鼻黏膜分泌過多）進行系統性文獻回顧
- 評估劑型與給藥途徑是否適合鼻腔疾病（目前路徑相容性尚未評估）
- 若文獻支持，再規劃小型探索性臨床試驗

**補充觀察：** 同批預測中，「急性喉咽炎」（分數 99.88%）與原適應症咽炎高度相關，較屬現有適應症的延伸，可作為優先研究的對照方向；其餘預測（外陰陰道念珠菌病、白喉、頸椎椎間盤退化）缺乏機轉與證據支持，建議維持 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

