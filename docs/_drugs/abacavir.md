---
layout: default
title: Abacavir
parent: 中證據等級 (L3-L4)
nav_order: 11
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Abacavir：預測新適應症為貓後天免疫缺乏症候群 (Feline acquired immunodeficiency syndrome)（證據等級 L4）。原適應症：HIV 感染、AIDS"
monitor_inn: "ABACAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Abacavir
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

## Abacavir：從 HIV 感染到貓免疫缺陷病毒感染（預測）
{: .text-alpha }

## 一句話總結

Abacavir 是核苷類逆轉錄酶抑制劑，原本用於治療 HIV 感染與 AIDS。
TxGNN 模型預測它可能對**貓後天免疫缺乏症候群 (Feline acquired immunodeficiency syndrome)** 有效，
目前**沒有臨床試驗**，僅有 **1 篇前臨床文獻**支持這個方向，證據偏弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染、AIDS（取自知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 貓後天免疫缺乏症候群 (Feline acquired immunodeficiency syndrome) |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏經核實的詳細作用機轉資料。就已知的藥理知識，abacavir 是核苷類逆轉錄酶抑制劑 (NRTI)，在細胞內被磷酸化為 carbovir triphosphate，與 dGTP 競爭並終止病毒 DNA 鏈延長。

貓免疫缺陷病毒 (FIV) 與 HIV 同屬慢病毒，同樣依賴逆轉錄酶複製。兩者在分子層面與臨床表現上相似，因此 FIV 常被用作 HIV 的動物模型，機轉上具有合理性。

不過需要注意：
- TxGNN 的高分很可能反映它與已核准 HIV 適應症的相似性，而非獨立的新證據。
- FIV 是獸醫疾病，沒有人類臨床開發路徑，對人類藥物再利用的意義有限。

另外兩個預測（皆為 Hold）：
- **猴免疫缺陷病毒 (SIV) 感染**（分數 99.79%，L4）：僅有 1 篇體外敏感性研究。SIV 主要是研究 HIV 的非人靈長類模型，不構成新的人類適應症。
- **伴有共濟失調步態、無語言能力及皮質白質減少的神經發育障礙**（分數 99.78%，L5）：無任何臨床試驗或文獻，僅為模型預測，機轉連結屬推測。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | 前臨床／動物研究（合併抗病毒療法） | Antiviral Research | 評估 zidovudine、lamivudine 與 abacavir 合併使用，對體外 FIV 複製的抑制效果。屬於合併用藥的間接證據，無法分離 abacavir 單藥的貢獻 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63701 | ZIAGEN TABLETS 300MG | — | — |
| HK-46236 | ZIAGEN ORAL SOLUTION 20MG/ML | — | — |
| HK-65647 | ABACAVIR TABLETS 300MG | — | — |
| HK-65610 | ABACAVIR TABLETS USP 300MG | — | — |
| HK-65625 | ABACAVIR/LAMIVUDINE SANDOZ TABLETS 600MG/300MG | — | — |

全部 10 張許可證均為有效狀態。

---

## 安全性考量

- **知識圖譜中標記的禁忌疾病**：肝衰竭、肝病、脂肪肝、非酒精性脂肪肝炎、腎臟疾病、胰臟炎、膽囊疾病、肌病／肌炎／皮肌炎、嗜中性白血球低下、顆粒球缺乏症、貧血、高三酸甘油脂血症、肥胖、乳酸中毒等（來自知識圖譜關聯，並非仿單文字）。
- **藥物交互作用**：共記錄 93 筆。其中中度等級包括 Naltrexone、Orlistat；其餘多數等級未明，例如 Metformin、Omeprazole、Pantoprazole、Morphine、Prednisone、Vancomycin、Amphotericin B。
- **已知安全顧慮**：HLA-B*57:01 相關過敏反應、心血管風險訊號，若考慮用於兒童神經發育族群需特別權衡。

其他警語與禁忌的正式仿單內容，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測的新適應症為獸醫疾病（FIV）或動物模型（SIV），沒有人類臨床開發路徑；唯一的證據是合併療法的前臨床研究。
- 預測分數高主要反映與原 HIV 適應症的相似性，不代表有新的治療機會。

**若要推進需要：**
- 確認是否有獸醫用藥的開發意圖與監管路徑。
- 取得 abacavir 單藥的 FIV 活性資料，區分其在合併療法中的貢獻。
- 取得詳細的作用機轉資料與香港仿單的警語、禁忌內容。
- 若對神經發育障礙的預測有興趣，須先找出疾病相關基因與路徑，並與 abacavir 的已知標的比對。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

