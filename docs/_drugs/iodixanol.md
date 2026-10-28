---
layout: default
title: Iodixanol
parent: 僅模型預測 (L5)
nav_order: 477
evidence_level: L5
indication_count: 2
monitor_inn: "Iodixanol"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis"]
last_modified_at: 2026-10-28
description: "Iodixanol：預測新適應症為退化性關節炎 (Osteoarthritis)（證據等級 L5）。原適應症：香港許可證未記載核准適應症文字"
---

# Iodixanol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Iodixanol：從（原適應症未記載）到退化性關節炎
{: .text-alpha }

## 一句話總結

Iodixanol 是一種含碘的等滲透壓顯影劑，在香港以 VISIPAQUE 品名上市。
TxGNN 模型預測它可能對**退化性關節炎 (Osteoarthritis)** 有效。
目前**沒有臨床試驗**，僅有 **5 篇文獻**，且都是把它當作影像檢查工具，並非治療證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未記載核准適應症文字 |
| 預測新適應症 | 退化性關節炎 (Osteoarthritis) |
| TxGNN 預測分數 | 0.9907 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Iodixanol 是含碘、等滲透壓的顯影劑，用於影像檢查，沒有證據顯示它具有改變疾病進程的藥理作用。

檢索到的文獻是把 iodixanol 當作診斷探針，例如用於關節軟骨的對比增強電腦斷層，以及研究溶質穿越軟骨與軟骨下骨界面的擴散。這些研究說明它能協助觀察退化性關節炎的軟骨狀態，但沒有顯示它能治療該疾病。

TxGNN 模型（深度學習）給出的高分（0.9907）可能反映模型從相關疾病之間學到的相似性，而非生物學證據。因此目前無法建立以機轉為基礎的合理性推論。

另一個預測的新適應症是類風濕性關節炎 (Rheumatoid Arthritis)，分數為 0.9900。唯一的文獻是另一種顯影劑 iohexol 的過敏脫敏病例報告，同樣沒有治療意義，證據等級為 L5，建議 Hold。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下文獻皆與退化性關節炎相關，但沒有任何一篇研究 iodixanol 的治療效果。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | 前臨床影像研究 | Annals of Biomedical Engineering | 利用奈米粒子擴散成像與電腦斷層，結合有限元素模型，呈現軟骨功能 |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | 前臨床影像研究 | Annals of Biomedical Engineering | 以光子計數電腦斷層與雙重顯影劑評估關節軟骨健康 |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | 電腦模擬（有限元素）研究 | Journal of Biomechanics | 以 iodixanol 作為中性擴散顯影劑，研究馬與人類樣本軟骨與軟骨下骨界面的通透性 |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | 電腦模擬（有限元素）研究 | Journal of Biomechanics | 以電腦斷層與雙相溶質模型，分析中性溶質穿越骨軟骨界面的傳輸 |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | 體外研究 | Journal of Experimental Orthopaedics | 含碘顯影劑在早期時間點不影響自體富含血小板血漿的功能 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43490 | VISIPAQUE INJ 320MG I/ML | 未記載 | 未記載 |
| HK-43491 | VISIPAQUE INJ 270MG I/ML | 未記載 | 未記載 |

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為部分列出的主要項目（嚴重等級為 Major）：
  - Metformin
  - Amphotericin B（含脂質複合體、膽固醇硫酸酯、脂質體等劑型）
  - Mesalazine、Balsalazide、Olsalazine、Sulfasalazine
  - Vancomycin
  - 胺基糖苷類抗生素：Kanamycin、Neomycin、Streptomycin
  - Polymyxin B
- 中等等級的項目包含 Mannitol。
- Famotidine、Acetylsalicylic acid、Morphine、Omeprazole、Prednisone 的交互作用等級為未知。

警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有檢索到的文獻都把 iodixanol 當作影像診斷工具，沒有任何研究直接評估它對退化性關節炎的治療效果，也沒有臨床試驗，因此證據等級為 L5。
- TxGNN 模型（深度學習）給出的高分可能反映模型從相關疾病之間學到的相似性，而非生物學證據。

**若要推進需要：**
- 補充作用機轉資料，並說明有何機轉可支持對退化性關節炎的治療作用
- 取得香港仿單，確認核准適應症、警語與禁忌症
- 有直接以 iodixanol 治療退化性關節炎的前臨床或臨床研究，才值得重新評估
- 若用於關節內注射，需先確認給藥途徑與劑型是否合適（目前路徑相容性尚未評估）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

