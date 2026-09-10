---
layout: default
title: Niraparib
parent: 高證據等級 (L1-L2)
nav_order: 526
evidence_level: L2
indication_count: 10
---

# Niraparib
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

# Niraparib：從卵巢癌維持治療到囊性腫瘤（子宮內膜漿液性癌）

## 一句話總結

Niraparib 是 PARP1/2 抑制劑，目前在其他市場核准用於復發性卵巢癌／輸卵管癌／原發性腹膜癌的維持治療，但**尚未在香港上市**。TxGNN 模型預測它可能對**囊性腫瘤 (Cystic Neoplasm)** 有效——此本體標籤實際對應到子宮內膜漿液性癌等囊性腫瘤，目前有 **3 個臨床試驗**（含 1 個正在招募的 Phase 2 試驗）與 **9 篇文獻**支持這個方向。

> 註：本次評估共產生 10 個候選適應症，其中 9 個（如 epiglottis neoplasm、良性口腔腫瘤等）TxGNN 分數雖與囊性腫瘤相近，但完全查無臨床試驗或文獻佐證、機轉亦難以合理外推，均列為 Hold（詳見文末）。本報告聚焦於證據等級最高的囊性腫瘤預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 卵巢癌／輸卵管癌／原發性腹膜癌（PARP 抑制劑維持治療）＊ |
| 預測新適應症 | 囊性腫瘤 (Cystic Neoplasm)，對應子宮內膜漿液性癌 |
| TxGNN 預測分數 | 99.99%（rank 519） |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

＊此原適應症資訊來自證據包中臨床試驗描述（如 NCT04716686 提及「FDA approved for maintenance treatment of adult patients with recurrent epithelial ovarian, fallopian...cancer」），非香港官方許可證資料——因 Niraparib 未在香港上市，無本地許可證可查。

## 為什麼這個預測合理？

證據包中正式的 MOA 欄位標記為資料缺口（DG002），但根據臨床試驗與文獻描述可確認：Niraparib 為 **PARP1/2 抑制劑**，其作用機轉是在具有同源重組修復缺陷（HRD）或 BRCA1/2 突變的腫瘤中，透過抑制 DNA 單股斷裂修復造成「合成致死 (synthetic lethality)」效果。

TxGNN 標記的「cystic neoplasm」本體標籤，實際上是子宮內膜漿液性癌 (Endometrial Serous Carcinoma, ESC) 等囊性婦科腫瘤的上位分類。文獻與試驗均指出，ESC 與高級別漿液性卵巢癌 (HGSOC) 在染色體不穩定性、體細胞拷貝數變異及體細胞突變上具有高度相似的分子特徵，臨床上 ESC 的治療策略也常參考 HGSOC 模式。

因此這並非全新的機轉假說，而是 Niraparib 既有的卵巢癌適應症，透過分子相似性延伸至同屬 HRD 相關的子宮內膜漿液性癌——機轉基礎相對紮實。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04716686](https://clinicaltrials.gov/study/NCT04716686) | Phase 2 | 招募中 | 83 | Niraparib 單藥用於子宮內膜漿液性癌之維持/復發治療，因其與高級別漿液性卵巢癌分子特徵相似而设計 |
| [NCT04159155](https://clinicaltrials.gov/study/NCT04159155) | Phase 2/3 | 已終止 | 11 | 加拿大多臂試驗，評估漿液性/p53 突變子宮內膜癌之前線與維持治療；因入組人數過低而終止 |
| [NCT05289648](https://clinicaltrials.gov/study/NCT05289648) | Early Phase 1 | 已撤回 | 0 | 探討術前 Niraparib 對高級別子宮內膜癌腫瘤組織的分子效應；已撤回，未產生數據 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40473279](https://pubmed.ncbi.nlm.nih.gov/40473279/) | 2025 | 臨床試驗方案 | BMJ Open | Niraparib 維持治療用於 Stage III/IV 化療初治復發或鉑敏感復發子宮漿液性癌之 Phase 2 研究方案 |
| [31851805](https://pubmed.ncbi.nlm.nih.gov/31851805/) | 2019 | Review | N Engl J Med | 漿液性卵巢癌一線治療之精準醫療綜述 |
| [41323499](https://pubmed.ncbi.nlm.nih.gov/41323499/) | 2025 | 基因體圖譜/世代研究 | Pathology Oncology Research | F1CDx 全面基因體檢測於 HGSOC 之技術表現與 PARP 抑制劑用藥建議整合 |
| [41520277](https://pubmed.ncbi.nlm.nih.gov/41520277/) | 2026 | 臨床前（類器官） | Cancer Biology & Therapy | 以高級別漿液性癌類器官/球體模型評估 carboplatin 併用 PARP 抑制劑之療效 |
| [40702505](https://pubmed.ncbi.nlm.nih.gov/40702505/) | 2025 | 生物資訊/預後模型 | Journal of Ovarian Research | 高級別漿液性卵巢癌幹細胞相關亞型與預後模型建立 |
| [31466953](https://pubmed.ncbi.nlm.nih.gov/31466953/) | 2019 | 病例報告 | BMJ Case Reports | 一例合併腦轉移之卵巢癌患者使用 Niraparib 維持治療案例 |
| [34321239](https://pubmed.ncbi.nlm.nih.gov/34321239/) | 2021 | 機轉/抗藥性研究 | Cancer Research | RAD51C 啟動子甲基化喪失導致 HGSOC 對 PARP 抑制劑產生抗藥性 |
| [41465250](https://pubmed.ncbi.nlm.nih.gov/41465250/) | 2025 | 蛋白質體學/機轉 | Int J Mol Sci | Olaparib、Niraparib、Rucaparib 於 HGSOC 細胞之多重藥理效應蛋白質體分析 |
| [41214101](https://pubmed.ncbi.nlm.nih.gov/41214101/) | 2025 | 機轉研究 | Scientific Reports | Claudin-4 於 HGSOC 中同時調控基因體穩定性與免疫逃逸之角色 |

## 香港上市資訊

Niraparib 目前未在香港取得藥品許可證（`total_licenses = 0`），無許可證資料可列。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（PARP1/2 抑制劑，非傳統細胞毒性化療藥物） |
| 骨髓抑制風險／致吐性分級／監測項目／處置防護 | 本證據包無相關毒性資料，請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單（本評估之關鍵警語、禁忌症與 DDI 資料均為缺口，已列為 Blocking 等級資料缺口 DG001）。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有一個正在招募的 Phase 2 試驗（NCT04716686）直接針對子宮內膜漿液性癌評估 Niraparib 單藥療效，且機轉上與其核准之卵巢癌適應症高度重疊（HRD/BRCA 相關合成致死）。
- 但尚無已完成之確證性研究結果，且該藥未在香港上市，安全性資料（DG001，Blocking）與正式 MOA（DG002）均缺失，不宜貿然推進。

**若要推進需要：**
- 取得 TFDA/香港仿單警語與禁忌症資料，解除 DG001（Blocking）
- 確認正式 MOA 文件（DrugBank API 查詢），解除 DG002
- 追蹤 NCT04716686、NCT04159155 之後續結果
- 其餘 9 個預測適應症（epiglottis neoplasm、良性頭頸部腫瘤、cervical neuroblastoma 等，多為 L5/Hold）證據不足或機轉錯位，暫不建議推進；其中「pre-malignant neoplasm」雖有 13 筆試驗但多為其他惡性腫瘤籃式試驗誤配（L4/S1，Research Question），可列為長期觀察項目
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

