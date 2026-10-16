---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluorouracil：預測新適應症為陰道葡萄狀胚胎型橫紋肌肉瘤 (botryoid-type embryonal rhabdomyosarcoma of the vagina)（證據等級 L5）。原適應症：胃癌、大腸癌轉移、胰臟腺癌、日光性角化症、淺表多發性基底細胞癌等"
monitor_inn: "Fluorouracil"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "liver sarcoma", "sickle cell-hemoglobin d disease syndrome", "sickle cell-hemoglobin c disease syndrome", "sickle cell-beta-thalassemia disease syndrome"]
---

# Fluorouracil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Fluorouracil：從胃癌與大腸癌等實體腫瘤到胚胎型橫紋肌肉瘤

## 一句話總結

Fluorouracil（5-FU）是一種嘧啶類抗代謝藥物，原本用於大腸癌轉移、胰臟腺癌、胃癌，以及外用於日光性角化症、基底細胞癌等皮膚病變。
TxGNN 模型預測它可能對**陰道葡萄狀胚胎型橫紋肌肉瘤 (botryoid-type embryonal rhabdomyosarcoma of the vagina)** 有效（預測分數最高）。
但這個預測目前**沒有任何臨床試驗**，也沒有直接針對該疾病的文獻支持，屬於僅有模型預測的階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃癌、大腸癌轉移、胰臟腺癌、日光性角化症、淺表多發性基底細胞癌等（香港許可證未載明核准適應症文字，此處依知識圖譜適應症整理） |
| 預測新適應症 | 陰道葡萄狀胚胎型橫紋肌肉瘤 (botryoid-type embryonal rhabdomyosarcoma of the vagina) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

> 備註：排名前 10 的預測中，有 7 項為橫紋肌肉瘤及其亞型，另有肝肉瘤與 3 種鐮狀細胞病症候群。以下證據章節以排名第 1 的預測為主，並在需要時補充其他預測的情況。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Fluorouracil 是胸苷酸合成酶抑制劑，屬嘧啶類抗代謝藥物，會干擾快速增殖細胞的 DNA/RNA 合成。因此在機轉上，它對增殖旺盛的腫瘤細胞具有一般性的細胞毒性。

橫紋肌肉瘤是兒童常見的軟組織肉瘤，細胞增殖快，理論上可能受抗代謝藥物影響。不過，Fluorouracil 並不是橫紋肌肉瘤標準療法（以 VAC/VAI 為基礎的方案）的成分，高分數較可能來自知識圖譜中與其他腫瘤的關聯，而非實際臨床證據。

其他預測也有類似情況。例如膽管橫紋肌肉瘤的預測，可能源自 Fluorouracil 在膽道癌的使用史。鐮狀細胞病的預測，則來自 Fluorouracil 實驗上可能誘導胎兒血紅素（類似 hydroxyurea）的推測，但其骨髓抑制與毒性使它遠不如既有選項。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

排名第 1 的預測（陰道葡萄狀胚胎型橫紋肌肉瘤）目前無相關文獻。下表為排名第 2 的預測「橫紋肌肉瘤」所對應的文獻，其中以小兒肉瘤與一般化療的回顧為主，沒有任何對照性證據。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Review | Cancer | 兒童肉瘤輔助化療的價值回顧，橫紋肌肉瘤約占兒童軟組織肉瘤一半 |
| [6277228](https://pubmed.ncbi.nlm.nih.gov/6277228/) | 1981 | Review | Ann Acad Med Singapore | 晚期癌症化療可治癒性的一般回顧，橫紋肌肉瘤列為可治癒的兒童癌症之一 |
| [42483493](https://pubmed.ncbi.nlm.nih.gov/42483493/) | 2026 | Case report | Case Rep Oncol Med | 19 歲男性舌部橫紋肌肉瘤；doxorubicin+ifosfamide 及 cisplatin+5-FU 均出現疾病進展，後續以 vincristine、actinomycin D 等方案治療 |
| [3951398](https://pubmed.ncbi.nlm.nih.gov/3951398/) | 1986 | Cohort | Med Pediatr Oncol | 兒童未分化鼻咽癌的治療經驗，與橫紋肌肉瘤無直接關聯 |

**解讀：** 唯一涉及 5-FU 的病例（PMID 42483493）顯示含 5-FU 方案未能控制疾病，並不支持其療效。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-40254 | FLUOROURACIL INJ 50MG/ML VIAL-PHARMACHEM（Teva） | 注射劑 | 未提供 |
| HK-45512 | 5-FLUOROURACIL INJ 50MG/ML (EBEWE)（Sandoz） | 注射劑 | 未提供 |
| HK-15219 | VERRUMAL SOLUTION EXTERNAL（Zuellig Pharma） | 外用溶液 | 未提供 |

三張許可證均為有效的單方製劑。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Fluoropyrimidine 類抗代謝藥） |
| 骨髓抑制風險 | 中度（知識圖譜將嗜中性白血球減少、血小板減少、白血球減少、顆粒球缺乏症列為相關風險疾病） |
| 致吐性分級 | 低至中度（依藥物類別判斷） |
| 監測項目 | CBC（含分類）、肝腎功能；並注意口腔黏膜炎與腹瀉 |
| 處置防護 | 注射劑需依細胞毒性藥物處置規範操作 |

詳細警語請參考原廠仿單。

---

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎疾病：** 腎臟疾病、肝臟疾病、膽囊疾病、血小板減少、嗜中性白血球減少、顆粒球缺乏症、白血球減少、腹瀉性疾病、活動性消化性潰瘍、咽炎、口腔炎、二氫嘧啶去氫酶 (DPD) 缺乏症。這些來自知識圖譜，並非仿單文字。
- **藥物交互作用：** 共查得 100 筆，以下為資料中標示的主要項目：
  - 中度：Metronidazole、Tinidazole
  - 輕度：Cimetidine、Levofloxacin
  - 其餘多數（如 Omeprazole、Pantoprazole、Metformin、Morphine 等）等級為未知

仿單的警語與禁忌文字尚未取得，正式評估前須補齊。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第 1 的預測僅有模型分數，沒有臨床試驗或直接文獻，證據等級為 L5。
- 唯一涉及 5-FU 的橫紋肌肉瘤病例顯示無效，且 5-FU 並非橫紋肌肉瘤標準療法，同時有明確的骨髓抑制與 DPD 缺乏等安全性風險。

**若要推進需要：**
- 取得 Fluorouracil 的作用機轉資料，並進行與橫紋肌肉瘤的機轉連結分析
- 取得香港仿單的警語、禁忌與核准適應症文字，完成安全性篩選
- 進行針對橫紋肌肉瘤（含 5-FU 的方案）的系統性文獻檢索與前臨床研究
- 與標準療法（VAC/VAI）比較，評估是否有臨床上的附加價值
- 若考慮其他預測，需另行評估：膽管橫紋肌肉瘤可參考膽道癌用藥經驗，鐮狀細胞病則需與 hydroxyurea 比較
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

