---
layout: default
title: Anagrelide
parent: 中證據等級 (L3-L4)
nav_order: 52
evidence_level: L4
indication_count: 2
---

# Anagrelide
{: .fs-9 }

證據等級: **L4** | 預測適應症: **2** 個
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

# Anagrelide：從原發性血小板增多症到反應性血小板增多症

## 一句話總結

Anagrelide（Agrylin）是一種 PDE3 抑制劑，原本用於降低骨髓增生性腫瘤（如原發性血小板增多症 Essential Thrombocythemia）患者的血小板數量。
TxGNN 模型預測它可能對**反應性血小板增多症 (Reactive Thrombocytosis)** 有效，預測分數高達 99.83%。
然而，目前**無相關臨床試驗**登記，現有 **10 篇文獻**均針對骨髓增生性腫瘤而非真正的反應性血小板增多症，此高分主要反映知識圖譜中的共享表型節點，而非真實臨床適用性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 原發性血小板增多症（Essential Thrombocythemia）及相關骨髓增生性腫瘤 |
| 預測新適應症 | 反應性血小板增多症 (Reactive Thrombocytosis) |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Anagrelide 是一種磷酸二酯酶 3（PDE3）抑制劑，透過抑制巨核細胞（megakaryocyte）的分化與成熟，選擇性降低血小板生成速率。此機轉理論上可降低**任何病因**所致的血小板升高，包括繼發性原因。

然而，反應性血小板增多症（Reactive Thrombocytosis）本質上是一種**繼發性、通常具自限性**的病態，常見於感染、慢性發炎、缺鐵性貧血、脾切除術後等情況。其血小板升高屬生理代償反應，標準治療策略為**處理潛在病因**，而非使用細胞減少療法直接壓制血小板。

TxGNN 的高分（0.998）主要反映知識圖譜中「thrombocytosis」為共享節點——原發性血小板增多症（ET）與反應性血小板增多症共享此表型節點，但兩者病理生理機轉截然不同。目前所有文獻幾乎均針對骨髓增生性腫瘤（ET/PV），此高分屬**預期中的計算性假陽性**，臨床實際適用性存疑。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | 回溯性研究 | Pediatric Blood & Cancer | 兒童原發性血小板增多症與反應性血小板增多症的比較，分析 12 例，Anagrelide 用於前者而非後者 |
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Review | Expert Review of Anticancer Therapy | Anagrelide 機轉與治療潛力更新：明確指出反應性血小板增多症不需治療介入，Anagrelide 適用於克隆性（clonal）血小板增多症 |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Review | Leukemia & Lymphoma | ET 及相關疾病中 Anagrelide 療法的批判性回顧：確認反應性血小板增多症與克隆性有本質差異 |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Review | American Journal of Medical Sciences | 血小板增多症臨床光譜分析：闡述血小板生成調控機轉及假性／反應性／克隆性之鑑別 |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Review | Medical Journal of Australia | ET 診斷依賴排除骨髓增生性疾病及反應性血小板增多症，降血小板療法適用於血小板 >1000×10⁹/L 的患者 |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Review | Leukemia Research | 血小板去除術（thrombocytapheresis）在骨髓增生性腫瘤極度血小板增多症中的角色，藥物細胞減少療法（含 Anagrelide）為主要選項 |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Review | Japanese Journal of Clinical Hematology | ET 診斷與治療：Anagrelide 列於抑制巨核細胞增殖的用藥選項之一 |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case Report | European Journal of Case Reports in Internal Medicine | ET 合併 Anagrelide 治療患者發生急性心肌梗塞 1 例，探討血栓風險管理 |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case Report | Srpski Arhiv | ET 合併僵直性脊椎炎病例，以 Anagrelide + DMARDs + etanercept 聯合治療；注意反應性輕至中度血小板增多症在僵直性脊椎炎中常見 |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case Report | Medicine | 脾切除術後血小板增多症患者成功進行斷指再植，提供血栓高風險情境下的處置指引 |

---

## 香港上市資訊

Anagrelide 目前**未在香港上市**，無任何登記許可證。如需使用，須透過特別用藥申請途徑取得。

---

## 安全性考量

安全性資訊請參考原廠仿單（Agrylin® 說明書）。

> 注意：本份 Evidence Pack 的警語、禁忌症及藥物交互作用資料均缺乏（Data Gap），建議於推進前優先補充 TFDA／EMA 仿單安全性資料。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 高預測分數（99.83%）係由知識圖譜中「thrombocytosis」共享節點所驅動，屬預期中的假陽性——反應性血小板增多症為繼發性、自限性疾病，其標準治療為處理潛在病因，而非直接降血小板細胞療法；現有 10 篇文獻均指向骨髓增生性腫瘤（ET/PV），無任何臨床試驗針對反應性血小板增多症評估 Anagrelide，且此藥在香港未取得上市許可。

**若要重新評估需要：**
- 確認是否存在特定亞族群（如脾切除後持續性、症狀性血小板增多症）可能受益的臨床前或機轉研究
- 補充完整安全性資料（警語、禁忌症、主要藥物交互作用）
- 評估是否有更具臨床合理性的替代再利用適應症（如其他 PDE3 相關疾病路徑）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

