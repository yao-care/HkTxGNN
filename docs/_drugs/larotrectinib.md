---
layout: default
title: Larotrectinib
parent: 中證據等級 (L3-L4)
nav_order: 438
evidence_level: L4
indication_count: 10
---

# Larotrectinib
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Larotrectinib：從 NTRK 融合陽性實體瘤 到 多發性內分泌腫瘤

## 一句話總結

Larotrectinib 是一款 TRK（tropomyosin receptor kinase）抑制劑，目前核准用於治療帶有 NTRK1/2/3 基因融合的實體腫瘤，與腫瘤原發部位無關。
TxGNN 模型預測它可能對**多發性內分泌腫瘤（Multiple Endocrine Neoplasia, MEN）**有效，
但目前僅有 **1 個間接相關的臨床試驗**和 **2 篇文獻**支持，證據等級偏低（L4），機轉關聯性也較薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | NTRK 基因融合陽性實體瘤（國際核准適應症；本地無許可證登記資料） |
| 預測新適應症 | Multiple Endocrine Neoplasia（多發性內分泌腫瘤） |
| TxGNN 預測分數 | 99.24% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Larotrectinib 詳細的作用機轉資料庫記錄（DrugBank MOA 欄位缺失）。根據證據包內的臨床試驗描述，Larotrectinib 是一種 TRK 抑制劑，透過阻斷 NTRK1/2/3 基因融合所產生的異常激酶活性來抑制腫瘤生長，其適應症判定不看腫瘤發生部位，只看是否帶有 NTRK 融合。

TxGNN 預測其對多發性內分泌腫瘤（MEN）有效，但這個預測的機轉合理性有限：MEN2（與甲狀腺髓質癌相關的亞型）主要驅動基因是 **RET**，並非 Larotrectinib 所標靶的 NTRK。只有在罕見的、同時帶有 NTRK 融合的甲狀腺癌病例中，才存在理論上的機轉關聯，整體證據基礎相當薄弱。

支持這個方向的資料，目前只有 1 個大型多臂籃式試驗（MATCH，依分子標記分派治療，並非針對 Larotrectinib+MEN 專門設計，相關性評為 C 級／間接相關）與 2 篇非直接相關的文獻。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | 進行中（未招募） | 6452 | MATCH 籃式試驗：依基因檢測結果將實體瘤/淋巴瘤/骨髓瘤患者分派至不同標靶藥物臂，非專為 Larotrectinib＋MEN 設計，僅間接相關（相關性 C 級） |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | 回顧晚期甲狀腺癌之激酶抑制劑治療現況（含多種藥物），非 Larotrectinib 專門研究 |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Preclinical/Mechanistic | NPJ Precision Oncology | 探討 RET 抑制劑（selpercatinib/pralsetinib）於 RET 驅動甲狀腺髓質癌之抗藥機轉，非 Larotrectinib 直接研究 |

## 香港上市資訊

Larotrectinib 目前**未於香港上市**，無許可證登記資料。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（TRK 酪胺酸激酶抑制劑），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項（證據包中僅間接提及血小板低下為已知不良反應，程度資料缺失） |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 建議監測 CBC（含血小板） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
目前僅有 1 個間接相關的大型籃式試驗和 2 篇非直接相關文獻支持，證據等級為 L4，且機轉關聯薄弱——MEN2 的主要驅動基因是 RET 而非 Larotrectinib 標靶的 NTRK，僅在罕見的 NTRK 融合陽性亞群才有理論基礎。

**若要推進需要：**
- 補齊 Larotrectinib 完整 MOA 與本地（香港）仿單安全性資料（現存 Blocking 級資料缺口：仿單警語/禁忌未取得）
- 篩選出真正帶有 NTRK 融合的 MEN／甲狀腺髓質癌病例證據，而非泛用籃式試驗結果
- 注意證據包中排名第 6 的候選適應症（PR 陰性乳癌、NTRK 融合驅動亞群）證據等級達 L2、決策階段已至 S2，且有 Larotrectinib 本尊的 Phase 2 basket trial（NCT02576431）直接支持，證據強度明顯優於本候選，建議優先評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

