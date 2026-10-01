---
layout: default
title: Trabectedin
parent: 高證據等級 (L1-L2)
nav_order: 877
evidence_level: L2
indication_count: 1
---

# Trabectedin
{: .fs-9 }

證據等級: **L2** | 預測適應症: **1** 個
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

# Trabectedin：從軟組織肉瘤與卵巢癌到女性乳癌

## 一句話總結

Trabectedin（商品名 Yondelis）是一種源自海洋被囊動物的抗腫瘤藥物。文獻指出它在歐洲已登記用於軟組織肉瘤，以及與微脂體 doxorubicin 併用治療卵巢癌。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效。
目前有 **2 個臨床試驗**和 **20 篇文獻**，但臨床試驗與乳癌的關聯有限，直接證據主要是 3 篇乳癌 Phase 2 研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

香港許可證資料未提供核准適應症，因此上表省略「原適應症」。

## 為什麼這個預測合理？

DrugBank 的作用機轉欄位目前缺資料，以下機轉說明來自文獻。Trabectedin 會結合 DNA 小溝，引發依賴轉錄偶聯核苷酸切除修復 (NER) 的 DNA 損傷。同源重組修復缺陷的細胞（例如 BRCA1/2 突變腫瘤）似乎對它更敏感。BRCA 缺陷相關文獻 (PMID 27710871) 與 olaparib 維持治療試驗都以此為依據。

Trabectedin 可能也會調節腫瘤微環境，例如減少腫瘤相關巨噬細胞。前臨床研究顯示，它在三陰性乳癌模型中能增強 IL-12 的抗腫瘤效果 (PMID 39777457)。

乳癌與卵巢癌都有一部分屬於 BRCA 相關、同源重組缺陷的腫瘤，這是兩者在機轉上最主要的連結。TxGNN 的 0.997 分只是計算預測，不能視為臨床證據。目前的支持來自 Phase 2 乳癌研究和機轉文獻，尚無 Phase 3 證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | 完成 | 9 | 在對 trabectedin 併用微脂體 doxorubicin 有反應後，以 olaparib 做維持治療（復發性卵巢癌）。屬於併用與維持治療設計，無法單獨評估 trabectedin 療效，與乳癌的關聯僅部分成立，需回登錄資料確認。 |
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | 完成 | 76 | 單盲、安慰劑對照，評估單次劑量 trabectedin 對晚期實體腫瘤患者 QT 間期的影響。屬藥理與安全性研究，非乳癌療效試驗。 |

這兩個試驗都不是乳癌療效的直接證據。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | Phase 2（隨機） | Clin Breast Cancer | 在曾接受 anthracycline 與 taxane 治療的晚期乳癌，比較兩種給藥方式的單藥 trabectedin。摘要僅說明評估療效與安全性，未列結果。 |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | Phase 2 | Clin Breast Cancer | 在 HR 陽性、HER2 陰性晚期乳癌，依 XPG 基因表現評估 trabectedin 1.3 mg/m² 每 3 週輸注。摘要未列結果。 |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Phase 2 | Ann Oncol | 在 BRCA1/2 種系突變的轉移性乳癌，評估 trabectedin 的療效與安全性。依據是 HR 缺陷腫瘤對它較敏感。 |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Phase 1 | Eur J Cancer | Trabectedin 併用 doxorubicin 的可行性與藥動學研究，納入 38 人（軟組織肉瘤 29、晚期乳癌 9）。對乳癌屬間接證據。 |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opin Investig Drugs | 回顧 trabectedin 用於乳癌。提到它主要影響轉錄調控，並可減少腫瘤相關巨噬細胞。 |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Review | Cancer Treat Rev | 探討 trabectedin 作為 BRCA 缺陷患者的化療選項。 |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | 前臨床 | Cancer Immunol Res | Trabectedin 可增強 IL-12 對三陰性乳癌的抗腫瘤效果，機轉為清除髓系抑制細胞並活化 NK 細胞。 |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | 體外研究 | Toxicol Lett | Trabectedin 在 MCF-7 與 MDA-MB-453 乳癌細胞中，以時間與濃度依賴方式誘導細胞毒性與凋亡。 |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | 體外研究 | Eur Cytokine Netw | 評估 trabectedin 對 HUVEC 與乳癌細胞的抗血管新生效果。 |
| [38366738](https://pubmed.ncbi.nlm.nih.gov/38366738/) | 2024 | 病例報告 | J Dermatol | Trabectedin 用於對多種抗癌藥難治的乳房放射線誘發血管肉瘤。此為肉瘤而非乳癌，屬間接證據。 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59078 | YONDELIS FOR INF 1MG | — | 未提供 |

製造商為 HIND WING CO LTD。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（海洋來源，DNA 小溝結合劑） |
| 骨髓抑制風險 | 高。文獻指出毒性以血液學與肝臟為主，約 50% 患者出現 3–4 級嗜中性白血球減少，約 20% 出現血小板減少 |
| 致吐性分級 | 中度（依藥物類別判斷，請以仿單為準） |
| 監測項目 | CBC（含分類）、肝功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 乳癌有 3 篇 Phase 2 研究，且有 BRCA 缺陷的機轉依據，證據等級為 L2。但已登錄的兩個試驗都不是乳癌療效的直接證據，也沒有 Phase 3 資料。
- 香港仿單的警語與禁忌資料缺失，屬阻斷性缺口，目前無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌症），完成安全性篩選
- 查詢 DrugBank 的作用機轉資料
- 取得上述 3 篇乳癌 Phase 2 研究的完整結果（反應率、存活期、安全性），評估實際療效
- 確認 NCT03470805 的收案族群是否包含乳癌
- 評估 BRCA1/2 突變、XPG 表現等生物標記對患者選擇的價值

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

