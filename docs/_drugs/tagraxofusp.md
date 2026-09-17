---
layout: default
title: Tagraxofusp
parent: 高證據等級 (L1-L2)
nav_order: 719
evidence_level: L2
indication_count: 10
---

# Tagraxofusp
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Tagraxofusp：從 BPDCN 到 CD123+ 前驅血液腫瘤

## 一句話總結

Tagraxofusp（SL-401）是 CD123（IL-3Rα）標靶白喉毒素融合蛋白，依據評估證據脈絡已核准用於母細胞性漿細胞樣樹突狀細胞腫瘤（BPDCN）。TxGNN 針對此藥產出 10 個高分預測適應症，但其中 8 個（包含分數最高的 esotropia）經機轉檢視後判定為**模型雜訊、無生物學合理性**；唯一具備實證支持的候選是**前驅惡性腫瘤 (Pre-malignant Neoplasm)**，目前有 **5 個臨床試驗**佐證 CD123 標靶邏輯可延伸至 AML/MDS/MPN 等血液系統前驅病灶。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | BPDCN（母細胞性漿細胞樣樹突狀細胞腫瘤）— 依臨床試驗摘要引述，非正式許可證資料 |
| 預測新適應症 | 前驅惡性腫瘤 (Pre-malignant Neoplasm) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Tagraxofusp 正式的 DrugBank MOA 欄位目前缺失，但依據 evidence pack 內臨床試驗（NCT05476770）摘要引述：「Tagraxofusp is a protein-drug conjugate consisting of a diphtheria toxin redirected to target CD123」，可確認其機轉為 CD123 標靶白喉毒素融合蛋白，透過結合 CD123 陽性細胞後遞送毒素達到細胞毒殺效果，已核准用於 BPDCN。

CD123 除了在 BPDCN 高度表現外，亦於部分骨髓性腫瘤的前驅病灶（如骨髓增生性腫瘤 MPN、高風險骨髓化生不良症候群 MDS）過度表現。多筆進行中或招募中的臨床試驗（SL-401/tagraxofusp 併用 azacitidine、venetoclax 或 pacritinib）正是針對這類 CD123+ 血液系統前驅/殘留病灶進行探索，顯示機轉上具延伸合理性。

需特別說明：「Pre-malignant Neoplasm」在此為 TxGNN 對血液腫瘤群集的**廣泛涵蓋標籤**，並非精確疾病實體，實際證據多集中於 AML 微小殘留病灶（MRD）、高風險 MDS、MPN 等具體亞群，推進前需進一步釐清目標族群。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05476770](https://clinicaltrials.gov/study/NCT05476770) | Phase 1 | 招募中 | 54 | Tagraxofusp 併用/不併用化療於復發/難治小兒 CD123+ 血液腫瘤 |
| [NCT07148180](https://clinicaltrials.gov/study/NCT07148180) | Phase 1/2 | 招募中 | 31 | Tagraxofusp + Azacitidine + Venetoclax 用於 AML 微小殘留病灶控制 |
| [NCT03113643](https://clinicaltrials.gov/study/NCT03113643) | Phase 1 | 招募中 | 72 | SL-401（即 tagraxofusp）併 Azacitidine/Venetoclax 用於復發/難治 AML、初治不適合標準誘導之 AML 及高風險 MDS |
| [NCT06414681](https://clinicaltrials.gov/study/NCT06414681) | Early Phase 1 | 尚未招募 | 20 | Tagraxofusp + Pacritinib 用於中高風險骨髓纖維化（JAK 抑制劑治療失敗/不適用族群） |
| [NCT03386513](https://clinicaltrials.gov/study/NCT03386513) | Phase 1/2 | 進行中未招募 | 179 | IMGN632（非同藥，CD123 標靶抗體藥物複合體）用於 AML/CD123+ 血液惡性腫瘤，間接佐證 CD123 標靶邏輯 |

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

目前未在香港取得藥品許可證，市場狀態為「未上市」。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶免疫毒素藥物（CD123 導向白喉毒素融合蛋白），非傳統化療藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。（仿單警語/禁忌資料屬 Blocking 等級資料缺口，尚未取得）

---

## 其他 TxGNN 預測（已判定為模型雜訊）

以下 8 個候選適應症雖 TxGNN 分數同樣接近 99.7%，但均無臨床試驗或文獻支持，且機轉檢視結果為「無生物學關聯」，判定為模型雜訊，不建議推進：

| 排名 | 疾病 | 分數 | 判定理由摘要 |
|------|------|------|-------------|
| 1 | Esotropia（內斜視） | 99.73% | 眼外肌調節異常，與 CD123 標靶機轉無關聯 |
| 3 | Inner ear neoplasm | 99.72% | CD123 表現於此腫瘤類型未見報導 |
| 4 | Benign neoplasm of tongue | 99.72% | 良性上皮腫瘤與 CD123 標靶無關 |
| 5 | Bronchial adenomas/carcinoids (childhood) | 99.72% | 類癌腫瘤通常不表現 CD123 |
| 6 | Ductal or ductular proliferation | 99.72% | 肝膽組織病理描述性名詞，無明確關聯 |
| 7 | Chondroid hamartoma | 99.72% | 良性錯構瘤與 CD123 表現無關 |
| 8 | Non-seminomatous lesion | 99.72% | 生殖細胞腫瘤未見 CD123 相關文獻 |
| 10 | Thyroglossal duct cyst | 99.72% | 先天性良性囊腫，與細胞毒殺標靶藥物機轉無關 |

---

## 結論與下一步

**決策：Hold**

**理由：**
「前驅惡性腫瘤」候選具備 L2 等級證據（5 個相關臨床試驗）及合理機轉延伸，但仿單警語/禁忌資料為 Blocking 等級缺口（DG001），無法完成安全性初評；藥物於香港亦尚未上市、無許可證資料。此外，TxGNN 為此藥物產出的 10 個候選中有 8 個經判定為模型雜訊，顯示本輪預測需先經人工機轉複核，不宜直接以最高分項目作為推進依據。

**若要推進需要：**
- 取得原廠仿單警語/禁忌資料（DG001，Blocking）
- 取得正式 DrugBank MOA 資料以完善機轉分析（DG002）
- 釐清「Pre-malignant Neoplasm」對應之具體目標族群（AML MRD / 高風險 MDS / MPN）並補充直接文獻佐證
- 評估香港藥品申請/上市可行性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

