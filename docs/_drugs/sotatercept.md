---
layout: default
title: Sotatercept
parent: 僅模型預測 (L5)
nav_order: 830
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sotatercept：預測新適應症為急性淋巴性白血病 (Acute Lymphoblastic Leukemia)（證據等級 L5）。原適應症：許可證資料未載明"
monitor_inn: "Sotatercept"
predicted_indications: ["acute lymphoblastic leukemia (disease)", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "drug-induced osteoporosis", "diabetic cataract", "HER2 positive breast carcinoma", "transitional cell carcinoma", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant"]
---

# Sotatercept
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

# Sotatercept：從（原適應症資料未提供）到急性淋巴性白血病

## 一句話總結

Sotatercept 是一種活化素受體 IIA 融合蛋白（activin receptor type IIA-Fc），在香港已有上市許可證，但本次compiled 的許可證資料未載明原核准適應症。
TxGNN 模型預測它可能對**急性淋巴性白血病 (Acute Lymphoblastic Leukemia)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 急性淋巴性白血病 (Acute Lymphoblastic Leukemia) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據本報告所整理的資訊，Sotatercept 是一種活化素受體 IIA-Fc 融合蛋白，作為活化素及其他 TGF-β 超家族配體（如 GDF）的「配體陷阱」。

活化素／TGF-β 訊號會影響造血作用與骨髓微環境，這是它與白血病之間唯一的理論連結。但此連結屬推測性質，沒有直接的機轉或臨床證據。0.998 的 TxGNN 分數僅是計算模型的預測結果，不能視為療效證據。

**其他預測適應症（皆為 L5，僅有模型預測）：**

| 排名 | 預測適應症 | TxGNN 分數 | 建議 | 簡述 |
|------|-----------|-----------|------|------|
| 2 | 重度非增殖性糖尿病視網膜病變 | 99.77% | Hold | TGF-β／活化素與視網膜血管重塑有關，但 Sotatercept 有出血相關不良事件（如鼻出血、微血管擴張），需專門評估 |
| 3 | 糖尿病視網膜病變 | 99.72% | Hold | 理由同上；血管性眼疾需特別謹慎 |
| 4 | 藥物誘發性骨質疏鬆 | 99.65% | Research Question | 活化素 A 抑制成骨細胞並促進破骨細胞生成；同類 ActRIIA-Fc 藥物在前臨床與早期人體研究中提高骨密度，機轉上最為合理 |
| 5 | 糖尿病白內障 | 99.49% | Hold | TGF-β 與水晶體上皮間質轉化有關，但全身性生物製劑用於此適應症的可行性存疑 |
| 6 | HER2 陽性乳癌 | 99.43% | Hold | 活化素訊號在腫瘤中具雙面性，抑制後的腫瘤學效應難以預測 |
| 7–10 | 泌尿上皮癌相關亞型（移行細胞癌、前列腺尿道泌尿上皮癌、腎盂肉瘤樣移行細胞癌、膀胱浸潤性肉瘤樣變異型） | 99.34%–99.39% | Hold | 僅有 TGF-β／EMT 的推測；相近分數可能反映本體論相近性，並非獨立佐證 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68795 | WINREVAIR POWDER FOR SOLUTION FOR INJECTION 60MG | 注射用粉劑 | 資料未載明 |
| HK-68794 | WINREVAIR POWDER FOR SOLUTION FOR INJECTION 45MG | 注射用粉劑 | 資料未載明 |
| HK-68792 | WINREVAIR POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 45MG | 注射用粉劑附溶劑 | 資料未載明 |
| HK-68793 | WINREVAIR POWDER AND SOLVENT FOR SOLUTION FOR INJECTION 60MG | 注射用粉劑附溶劑 | 資料未載明 |

上述 4 張許可證均為單方製劑，狀態有效，持證商為 MERCK SHARP & DOHME (ASIA) LTD。

---

## 安全性考量

安全性資訊請參考原廠仿單。

另外，針對各預測適應症的評估提示：Sotatercept 與出血相關不良事件（如鼻出血、微血管擴張）有關，若考慮用於視網膜血管疾病，需專門評估；用於腫瘤時，活化素訊號在部分情境具腫瘤抑制作用，抑制後的腫瘤學效應難以預測。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（急性淋巴性白血病）僅有 TxGNN 模型分數，無任何臨床試驗或文獻，證據等級為 L5，機轉連結也屬推測。
- 在所有預測中，藥物誘發性骨質疏鬆的機轉最合理，可作為研究問題（Research Question）優先探討。

**若要推進需要：**
- 補齊香港仿單的核准適應症、警語與禁忌症資料
- 取得詳細的作用機轉資料
- 針對首要預測及藥物誘發性骨質疏鬆進行系統性文獻與試驗檢索，並設計前臨床驗證
- 針對出血風險及對骨骼、血管與腫瘤組織的影響，建立專門的安全性評估計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

