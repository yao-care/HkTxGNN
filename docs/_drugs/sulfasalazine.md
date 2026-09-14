---
layout: default
title: Sulfasalazine
parent: 中證據等級 (L3-L4)
nav_order: 712
evidence_level: L3
indication_count: 5
---

# Sulfasalazine
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Sulfasalazine：從類風濕性關節炎到骨關節炎（Osteoarthritis）

## 一句話總結

Sulfasalazine（DB00795）長期用於類風濕性關節炎與發炎性腸道疾病的抗發炎治療（依本評估資料包內文獻脈絡佐證，非結構化欄位提供）。
TxGNN 模型對本藥物產出多個高分預測，其中僅**骨關節炎 (Osteoarthritis)** 有實質證據支持，
目前有 **2 個臨床試驗**（皆非直接測試 sulfasalazine 於 OA）與 **9+ 篇相關文獻**（以體外/動物模型為主）。
其餘 4 個更高分的預測（如短指併指症候群等罕見遺傳疾病）經機轉評估後判定為知識圖譜偽陽性，無臨床意義。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎（依文獻佐證推論，資料包未提供結構化原適應症欄位） |
| 預測新適應症 | 骨關節炎 (Osteoarthritis) |
| TxGNN 預測分數 | 99.64%（rank 7135） |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為資料缺口，DG002）。根據文獻內容，Sulfasalazine 及其代謝物（5-ASA、sulfapyridine）已知可抑制 NF-κB 通路、降低 IL-1/TNF-α 等促發炎細胞激素釋放，並在多篇體外與動物模型研究中證實可下調軟骨基質金屬蛋白酶（MMP）活性、減少蛋白聚糖與膠原蛋白流失，對軟骨具保護作用（見 PMID 19690126、26466556、24329131）。

骨關節炎雖傳統上被視為退化性疾病，但近年病理生理學已確立其低度發炎（low-grade inflammation）與軟骨基質降解的角色，這與 sulfasalazine 的抗發炎/軟骨保護機轉在理論上有合理連結。然而，現有證據幾乎全部來自體外、細胞或動物模型，**尚無任何針對人類 OA 病人族群設計的臨床試驗**直接測試 sulfasalazine 的療效，現有兩個臨床試驗實際上是評估其他藥物（CRx-102、tofacitinib+MTX）於 RA 族群，僅背景相關。

> ⚠️ **其他 4 個高分預測為知識圖譜偽陽性**：短指併指症候群、缺損性小眼球-根性肢端發育不良症候群、OA 遺傳易感性、先天性稀毛併幼年型黃斑部退化症等，TxGNN 分數雖高達 99.6%–99.9%，但皆為罕見先天發育性/遺傳性疾病，與 sulfasalazine 已知的抗發炎機轉無生物學關聯，且完全無臨床試驗或文獻佐證，應視為節點鄰近性造成的雜訊，不建議進一步評估。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00551707](https://clinicaltrials.gov/study/NCT00551707) | Phase 2 | 完成 | 51 | 評估 CRx-102（dipyridamole+低劑量 prednisolone）於活動性 RA，**未使用 sulfasalazine**，相關性中等（Grade B） |
| [NCT03975790](https://clinicaltrials.gov/study/NCT03975790) | N/A | 完成 | 479 | Xeljanz（tofacitinib）+MTX 停用 vs 續用之真實世界比較研究，**未使用 sulfasalazine**，相關性低（Grade C） |

⚠️ 目前無直接測試 sulfasalazine 用於 OA 病人的臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29548914](https://pubmed.ncbi.nlm.nih.gov/29548914/) | 2018 | Preclinical (in vitro/動物) | Int J Biol Macromol | SASP-玻尿酸複合物於 OA 大鼠模型可抑制發炎並減緩軟骨退化 |
| [26466556](https://pubmed.ncbi.nlm.nih.gov/26466556/) | 2016 | Preclinical (動物模型) | J Orthop Res | Sulfasalazine 透過抑制 cystine/glutamate 反向轉運體，減緩 ACLT+MMx 誘發之軟骨破壞 |
| [19690126](https://pubmed.ncbi.nlm.nih.gov/19690126/) | 2009 | Preclinical (軟骨外植體) | Rheumatology | Sulfasalazine 阻斷細胞激素刺激下的蛋白聚糖/膠原蛋白釋放，下調 MMP |
| [24329131](https://pubmed.ncbi.nlm.nih.gov/24329131/) | 2014 | Preclinical (軟骨細胞蛋白質體) | Mod Rheumatol | Sulfasalazine 與 tofacitinib 對關節軟骨細胞蛋白質表現的影響 |
| [12205730](https://pubmed.ncbi.nlm.nih.gov/12205730/) | 2002 | Clinical (RA 病人) | Yonsei Med J | Sulfasalazine 治療對 RA 病人尿液膠原交聯排出量（結締組織代謝標記）之影響 |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | Preclinical (人類滑膜組織) | Wien Klin Wochenschr | Sulfasalazine 及其代謝物抑制 OA/RA 病人滑膜組織之 LTC4 釋放 |
| [35958605](https://pubmed.ncbi.nlm.nih.gov/35958605/) | 2022 | Review | Front Immunol | 發炎性關節炎（含 OA）中鐵死亡機轉之回顧 |
| [11478054](https://pubmed.ncbi.nlm.nih.gov/11478054/) | 2001 | Review | Hand Clinics | RA 與 OA 藥物治療現況回顧 |
| [9567207](https://pubmed.ncbi.nlm.nih.gov/9567207/) | 1998 | Review | Curr Opin Rheumatol | 風濕性疾病臨床試驗更新回顧（含 OA） |

---

## 其他 TxGNN 預測（低置信度，建議忽略）

| 疾病 | TxGNN 分數 | 證據等級 | 評估 |
|------|-----------|---------|------|
| 短指併指症候群 (Brachydactyly-syndactyly syndrome) | 99.94% | L5 | 罕見骨骼發育基因缺陷，與抗發炎機轉無關，判定為偽陽性 |
| 缺損性小眼球-根性肢端發育不良症候群 | 99.94% | L5 | 罕見先天眼部/骨骼發育畸形，與 sulfasalazine 機轉無關 |
| 骨關節炎易感性（遺傳） | 99.88% | L5 | GWAS 本體論詞條，非可介入之臨床表現型 |
| 先天性稀毛併幼年型黃斑部退化症 | 99.66% | L5 | 遺傳性毛髮/視網膜退化症候群，機轉無關 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

⚠️ 本資料包標記兩項待補資料缺口：
- **TFDA/香港衛生署仿單警語與禁忌**（Blocking，DG001）— 缺此資料無法進入 S1 安全性初評
- **完整作用機轉資料**（High，DG002）— 需查詢 DrugBank API 補齊

---

## 結論與下一步

**決策：Hold**

**理由：**
骨關節炎預測具機轉合理性，且有多篇體外/動物模型研究支持 sulfasalazine 之軟骨保護與抗發炎作用，但缺乏針對 OA 病人族群的直接臨床試驗數據，現有臨床試驗皆非以 sulfasalazine 為介入藥物。其餘 4 個更高分預測經評估為知識圖譜偽陽性，無需進一步行動。

**若要推進需要：**
- 補齊 TFDA/香港衛生署仿單警語與禁忌資料（DG001，Blocking，S1 安全性初評前置條件）
- 透過 DrugBank API 補齊完整 MOA 資料（DG002）
- 尋找或設計針對 OA 病人族群的前瞻性臨床試驗（目前證據僅止於體外/動物模型）
- 確認香港上市可行性（目前 sulfasalazine 於香港未上市，需評估藥證申請路徑）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

