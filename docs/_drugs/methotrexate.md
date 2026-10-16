---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 571
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Methotrexate：預測新適應症為肺母細胞瘤 (Pulmonary Blastoma)（證據等級 L5）。原適應症：急性淋巴母細胞白血病、非何杰金氏淋巴瘤、類風濕性關節炎、乾癬、蕈樣肉芽腫等"
monitor_inn: "METHOTREXATE"
predicted_indications: ["pulmonary blastoma", "primary pulmonary lymphoma", "small cell lung carcinoma", "well-differentiated fetal adenocarcinoma of the lung", "Hodgkins lymphoma"]
---

# Methotrexate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Methotrexate：從急性淋巴母細胞白血病／類風濕性關節炎／淋巴瘤到肺母細胞瘤

## 一句話總結

Methotrexate（甲氨蝶呤）是已上市多年的抗代謝藥物，原本用於急性淋巴母細胞白血病、淋巴瘤、類風濕性關節炎與乾癬等。
TxGNN 模型預測它可能對**肺母細胞瘤 (Pulmonary Blastoma)** 有效，但目前**沒有臨床試驗和文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性淋巴母細胞白血病、非何杰金氏淋巴瘤、類風濕性關節炎、乾癬、蕈樣肉芽腫等（來自知識圖譜；香港許可證未提供適應症文字） |
| 預測新適應症 | 肺母細胞瘤 (Pulmonary Blastoma) |
| TxGNN 預測分數 | 99.45% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張（皆為有效單方許可證） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Methotrexate 是一種抗葉酸藥物（antifolate），可抑制 DHFR 酶，對快速分裂的細胞具有細胞毒性。它在淋巴瘤與白血病等血液惡性腫瘤中的療效已被證實，因此機轉上可能適用於增生快速的惡性腫瘤。

肺母細胞瘤是罕見的肺部惡性腫瘤。模型給出高分，主要反映 Methotrexate 與各類腫瘤之間的整體網路關聯。除了「一般細胞毒性化療」這個推論外，沒有任何針對肺母細胞瘤的證據，也沒有說明為何此藥對該腫瘤特別適用。這個預測應視為待驗證的假說，而非臨床建議。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 8 張有效許可證，以下列出 5 張（皆為單方製劑，許可證資料未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-29818 | METHOTREXAT-EBEWE CONC FOR IV INF 5000MG | Sandoz Hong Kong Limited |
| HK-67078 | METHOTREXATE TABLETS 2.5MG | Hong Kong Medical Supplies Ltd |
| HK-16293 | METHOTREXATE INJ 50MG/2ML | Pfizer Corporation Hong Kong Limited |
| HK-36225 | METHOTREXAT TAB 2.5MG (EBEWE) | Sandoz Hong Kong Limited |
| HK-27062 | EMTHEXATE TAB 2.5MG | Teva Pharmaceutical Hong Kong Limited |

香港同時有口服錠劑與注射劑型的產品。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（抗葉酸／抗代謝類） |
| 骨髓抑制風險 | 高（知識圖譜顯示白血球減少、血小板減少、貧血為相關禁忌狀況） |
| 致吐性分級 | 低至中度，依劑量而異（高劑量時風險較高） |
| 監測項目 | CBC（含分類）、肝功能、腎功能；高劑量治療時另需監測血中藥物濃度 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

詳細警語與劑量調整請參考原廠仿單。

---

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎的疾病**（非仿單內容）：肝衰竭、肝臟疾病、腎臟疾病、膽囊疾病、胃潰瘍／消化性潰瘍、潰瘍性結腸炎／發炎性腸道疾病、血小板減少、白血球減少、貧血（含巨球性貧血）、間質性肺病、肺纖維化、口腔炎、免疫系統疾病、物質濫用／依賴、膿輸尿管。
- **藥物交互作用**：共查得 100 筆。
  - **Major 等級**：Rabeprazole、Amoxicillin、Acetylsalicylic acid（阿斯匹靈）。
  - **Moderate 等級（部分）**：Doxycycline、Tetracycline、Clarithromycin、Mesalazine、Balsalazide、Amphotericin B、Bupropion、Pioglitazone、Acarbose，以及多種類固醇（Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide）。
  - **Minor 等級**：Potassium citrate。

香港仿單的警語與禁忌尚未取得，正式評估前必須補齊。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 肺母細胞瘤的預測分數雖高（99.45%），但沒有任何臨床試驗或文獻，證據等級僅為 L5，且缺乏機轉資料與仿單安全性資料。
- 本報告彙整的其他預測中，**何杰金氏淋巴瘤**有較多證據（證據等級 L2、44 個相關試驗），可作為後續優先評估的方向。不過其中多為多藥化療或移植預防 GVHD 的方案，Methotrexate 的單獨貢獻無法判斷。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與適應症文字，完成基本安全性篩選。
- 補充 DrugBank 的作用機轉資料。
- 系統性搜尋肺母細胞瘤的病例報告與治療文獻，確認是否有 Methotrexate 的實際使用紀錄。
- 評估該罕見腫瘤的現行標準治療，判斷 Methotrexate 是否有臨床定位。
- 若要轉向證據較多的預測（如何杰金氏淋巴瘤），需另行評估並釐清 Methotrexate 在現行治療中的角色。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

