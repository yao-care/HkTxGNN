---
layout: default
title: Mesalazine
parent: 高證據等級 (L1-L2)
nav_order: 404
evidence_level: L2
indication_count: 5
---

# Mesalazine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Mesalazine：從潰瘍性結腸炎到類風濕性關節炎

## 一句話總結

Mesalazine（5-胺基水楊酸，5-ASA）是廣泛用於**潰瘍性結腸炎**的抗發炎藥物。
TxGNN 模型針對此藥共產生 5 個預測適應症，其中證據支持度最高的是**類風濕性關節炎 (Rheumatoid Arthritis)**，
目前有 **6 個相關臨床試驗**（其中 2 個與適應症直接相關）與 **20 篇文獻**可供評估，但證據強度存在關鍵爭議，詳見下文。

> **重要提醒**：TxGNN 原始分數最高的預測（congenital hypotrichosis with juvenile macular dystrophy，先天性稀毛合併幼年黃斑部退化症）完全沒有臨床試驗或文獻佐證，且與 5-ASA 之抗發炎機轉無已知關聯，評估報告已將其排除，改以證據等級最高的候選項目作為本報告主軸。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 潰瘍性結腸炎（Ulcerative Colitis，依現有文獻推定） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.57%（第 7999 名） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 收錄之詳細作用機轉資料（MOA 為資料缺口，DG002）。根據現有文獻，Mesalazine（5-ASA）具有抑制前列腺素（PGE2）與白三烯（LTB4、LTC4）合成、抑制 NF-κB 路徑及調節發炎細胞激素（IL-1β、TNF-α）與基質金屬蛋白酶（MMP）表現等抗發炎特性，這些機轉理論上不限於腸道，也可能作用於關節滑膜發炎。

潰瘍性結腸炎與類風濕性關節炎同屬免疫介導之慢性發炎性疾病。事實上歷史發展順序恰好相反：5-ASA 最初是在 1940 年代為了治療風濕性多關節炎而開發，其後才意外發現對潰瘍性結腸炎有效，因而轉向腸胃科領域發展（PMID 17708602）。以 5-ASA 為活性代謝物的 Sulfasalazine，至今仍是 RA 的第二線 DMARD（疾病修飾抗風濕藥物）（PMID 7588084）。

然而，這正是本預測最關鍵的爭議所在：多篇 1980-1990 年代的頭對頭比較研究（PMID 2860942、2877851、8535642）直接將 Sulfasalazine 拆解為 Sulfapyridine 與 5-ASA 兩個成分分別測試，結果一致顯示 **Sulfapyridine（而非 5-ASA/Mesalazine）才是主要的抗風濕活性成分**，5-ASA 單獨使用僅呈現微弱的一線效果，未見顯著疾病修飾作用。換言之，現有臨床證據多半是建立在 Sulfasalazine（複方/前驅藥）身上，並不能直接等同於 Mesalazine 本身對 RA 有效。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02930343](https://clinicaltrials.gov/study/NCT02930343) | Phase 3 | 已終止 | 136 | 比較 Sulfasalazine 與 Leflunomide 併用 DMARD 治療 Methotrexate 失效之 RA 患者，疾病與適應症直接對應，但試驗提前終止，且受試藥物為 Sulfasalazine 而非純 Mesalazine |
| [NCT00637780](https://clinicaltrials.gov/study/NCT00637780) | Phase 4 | 已終止 | 2 | Sulfasalazine 緩釋錠於幼年型特發性關節炎兒童之藥動學特徵化研究，樣本僅 2 人且已終止，僅供安全性/藥動參考，非療效試驗 |

**排除說明**：檢索另命中 4 個試驗（NCT05580861、NCT03591770、NCT00514982、NCT06201793），經評估分別為急性骨髓性白血病誘導化療、潰瘍性結腸炎疫苗免疫原性研究、Hermansky-Pudlak 症候群相關腸炎（已撤回）、Minocycline 治療潰瘍性結腸炎研究，皆與 Mesalazine 治療 RA 無直接關聯，判定為資料連結錯誤，未列入上表。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2860942](https://pubmed.ncbi.nlm.nih.gov/2860942/) | 1985 | Cohort | BMJ (Clin Res Ed) | 分別測試 Sulphapyridine 與 5-ASA：Sulphapyridine 有明顯二線抗風濕效果，5-ASA 僅具微弱一線效果 |
| [2877851](https://pubmed.ncbi.nlm.nih.gov/2877851/) | 1986 | Preclinical | Drugs | 開放性研究：Sulphasalazine 組多數疾病活性指標顯著改善，單用 5-ASA 組未見改善 |
| [8535642](https://pubmed.ncbi.nlm.nih.gov/8535642/) | 1995 | Review | Br J Rheumatol | 回顧指出多數證據支持 Sulphapyridine（而非 5-ASA）為 Sulphasalazine 治療 RA 之主要活性成分，也是主要副作用來源 |
| [7588084](https://pubmed.ncbi.nlm.nih.gov/7588084/) | 1995 | Review | Drugs | Sulfasalazine 藥理學與 RA 療效總覽：自 1940 年代起確立為 DMARD，但活性分子歸屬仍有爭議 |
| [2899645](https://pubmed.ncbi.nlm.nih.gov/2899645/) | 1988 | Cohort | J Rheumatol | Sulfasalazine 治療 12 週後使 RA 患者異常活化淋巴球恢復正常，提示免疫調節機轉 |
| [10743803](https://pubmed.ncbi.nlm.nih.gov/10743803/) | 2000 | Mechanistic | J Rheumatol | SASP 及其代謝物（含 5-ASA）可調節 RA 滑膜纖維母細胞之發炎細胞激素（IL-1β、TNF-α）與 MMP mRNA 表現 |
| [7904547](https://pubmed.ncbi.nlm.nih.gov/7904547/) | 1993 | Review | Clin Pharmacokinet | 慢作用抗風濕藥物（含 Sulphasalazine）藥動學回顧：起效延遲數月，個體差異大 |
| [41443863](https://pubmed.ncbi.nlm.nih.gov/41443863/) | 2025 | Case report | Intern Med (Tokyo) | RA 患者使用 Mesalazine 後出現 5-ASA 誘發性結腸炎個案，藥物誘導淋巴球刺激試驗陽性，提示安全性訊號 |
| [12235076](https://pubmed.ncbi.nlm.nih.gov/12235076/) | 2002 | Review | Gut | Sulphasalazine 與 Mesalazine 嚴重不良反應再評估（英國藥物安全委員會通報資料） |
| [17708602](https://pubmed.ncbi.nlm.nih.gov/17708602/) | 2007 | Review | World J Gastroenterol | 回顧指出 5-ASA 最初為治療 RA 而設計，後意外發現對潰瘍性結腸炎有效，因而轉向 IBD 領域發展 |

---

## 香港上市資訊

目前 Mesalazine 在香港**未上市**（許可證數：0），無可列示之許可證資料。

---

## 其他 TxGNN 預測候選（供參考）

| 排名 | 預測適應症 | 證據等級 | 建議 | 備註 |
|------|-----------|---------|------|------|
| 2 | 骨關節炎 (Osteoarthritis) | L4 | Research Question | 有 3 篇機轉/體外/生物資訊層級文獻（含 PMID 38310093 OSCAR-PPARγ 軸機轉），但完全無人體臨床試驗，僅屬臨床前假說 |
| 1 | 先天性稀毛合併幼年黃斑部退化症 | L5 | Hold | 無任何試驗或文獻，機轉上與 5-ASA 無重疊，判定為知識圖譜雜訊 |
| 4 | 脂漏性角化症 (Seborrheic Keratosis) | L5 | Hold | 良性增生性病灶，非發炎性疾病，與 5-ASA 機轉無合理連結 |
| 5 | 骨關節炎易感性 (OA Susceptibility) | L5 | Hold | 屬遺傳風險性狀而非可治療疾病實體，建議與骨關節炎條目合併或移除 |

---

## 安全性考量

安全性資訊請參考原廠仿單。目前 TFDA/香港仿單警語與禁忌資料尚未取得（見下方資料缺口說明），無法完成安全性初評。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Mesalazine 對 RA 的預測有 L2 等級證據支撐，且有明確的歷史發展脈絡（5-ASA 最初即為治療 RA 而開發），並非憑空預測。
- 但現有幾乎所有正面臨床證據（含唯一的 Phase 3 試驗 NCT02930343）針對的是 **Sulfasalazine 複方**，而多篇頭對頭藥理學研究（PMID 2860942、2877851、8535642）明確指出 5-ASA/Mesalazine 單獨使用之抗風濕效果微弱，真正活性成分可能是 Sulfapyridine 代謝物。此為推進前必須解決的核心科學問題，故不建議直接 Go。

**若要推進需要：**
- 取得 TFDA/香港仿單警語與禁忌資料（DG001，**Blocking**，目前無法進入 S1 安全性初評）
- 補齊 DrugBank 作用機轉完整資料（DG002，High，影響機轉關聯性分析之可信度）
- 釐清 5-ASA（Mesalazine）獨立於 Sulfapyridine 之抗風濕活性，建議先進行體外/動物模式之頭對頭比較研究
- 若確認機轉合理，需設計以**純 Mesalazine**（非 Sulfasalazine 複方）為受試藥物之 RA 對照試驗，現有 NCT02930343、NCT00637780 均不符此條件
- 確認香港上市可行性（目前 0 張許可證，尚未上市）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

