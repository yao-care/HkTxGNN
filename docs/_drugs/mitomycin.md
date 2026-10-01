---
layout: default
title: Mitomycin
parent: 僅模型預測 (L5)
nav_order: 584
evidence_level: L5
indication_count: 5
---

# Mitomycin
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

# Mitomycin：從胰臟腺癌（許可證未載明，待仿單確認）到胰臟骨質細胞巨細胞瘤

## 一句話總結

Mitomycin（絲裂黴素）是 DNA 交聯型烷化類細胞毒性藥物。香港四張許可證的適應症欄位皆為空白，但模型推論其標示用途為播散性胰臟腺癌。
TxGNN 預測它可能對**胰臟骨質細胞巨細胞瘤 (Osteoclastic giant cell tumor of pancreas)** 有效。
目前**沒有臨床試驗**和**沒有文獻**支持這個預測，僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明（依藥物類別推論為播散性胰臟腺癌，需以仿單確認） |
| 預測新適應症 | 胰臟骨質細胞巨細胞瘤 (Osteoclastic giant cell tumor of pancreas) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。已知 Mitomycin 是 DNA 交聯型烷化劑，會抑制腫瘤細胞的 DNA 複製而產生細胞毒性。

模型給出高分，最可能反映的是「Mitomycin 與胰臟腺癌」的類別層級關聯。這種關聯不針對這個罕見、組織學上獨特的亞型，所以分數高不代表對此亞型有效。

現有資料中沒有任何試驗或文獻直接評估 Mitomycin 對這個亞型的作用，因此這個預測目前只能視為假說。

### 同批預測的其他胰臟腫瘤適應症

同一批預測還有以下 4 個胰臟腫瘤適應症，依據同樣是類別層級的關聯，也都沒有臨床試驗。

| 排名 | 預測適應症 | 分數 | 證據等級 | 備註 |
|------|-----------|------|---------|------|
| 2 | 胰臟實性假乳突癌 (Solid pseudopapillary carcinoma of pancreas) | 99.86% | L5 | 此腫瘤多為低惡性度，以手術切除為主，加入全身性化療的理由薄弱 |
| 3 | 胰臟混合分化癌 (Pancreatic carcinoma with mixed differentiation) | 99.85% | L5 | 腺癌成分與原適應症有非特異性關聯 |
| 4 | 胰臟導管內乳突黏液癌 (Pancreatic intraductal papillary-mucinous carcinoma) | 99.85% | L4 | 僅有 1 篇 2005 年病例報告，非療效證據 |
| 5 | 胰臟混合導管–內分泌癌 (Mixed ductal-endocrine carcinoma of pancreas) | 99.85% | L5 | 內分泌成分沒有支持 Mitomycin 的理由 |

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67642 | ACCORD MITOMYCIN 2 POWDER FOR SOLUTION FOR INJECTION/INFUSION OR INTRAVESICAL USE 2MG | 注射／輸注／膀胱內灌注用粉末 | 許可證資料未載明 |
| HK-67641 | ACCORD MITOMYCIN 10 POWDER FOR SOLUTION FOR INJECTION/INFUSION OR INTRAVESICAL USE 10MG | 注射／輸注／膀胱內灌注用粉末 | 許可證資料未載明 |
| HK-66821 | MITONCO POWDER FOR SOLUTION FOR INJECTION 10MG | 注射用粉末 | 許可證資料未載明 |
| HK-67651 | MITOMYCIN FOR INJECTION USP 10MG | 注射用粉末 | 許可證資料未載明 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（DNA 交聯型烷化劑） |
| 骨髓抑制風險 | 高（此類藥物以延遲性、累積性骨髓抑制聞名；本資料包未提供 toxicity 資料，此為藥物類別的一般認知） |
| 致吐性分級 | 低至中度（依藥物類別判斷） |
| 監測項目 | CBC（含分類與血小板）、腎功能、肝功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

以上項目缺乏原廠資料佐證，請參考原廠仿單的警語與注意事項。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數支持，沒有臨床試驗和文獻，證據等級為 L5。
- 高分主要來自類別層級的關聯，並非針對這個罕見亞型。
- 香港許可證的適應症和仿單警語資料都缺漏，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衞生署核准的仿單，確認原適應症、警語與禁忌症
- 從 DrugBank 補齊作用機轉（MOA）資料
- 檢索 Mitomycin 用於胰臟骨質細胞巨細胞瘤的病例報告、回顧性研究或前臨床研究
- 由臨床專家評估此亞型使用全身性 DNA 交聯劑的合理性，以及給藥途徑是否相容
- 若後續出現直接證據，再重新評估並考慮升級為 Proceed with Guardrails

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

