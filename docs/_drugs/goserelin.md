---
layout: default
title: Goserelin
parent: 高證據等級 (L1-L2)
nav_order: 359
evidence_level: L1
indication_count: 3
---

# Goserelin
{: .fs-9 }

證據等級: **L1** | 預測適應症: **3** 個
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

# Goserelin：從 乳癌輔助治療 到 閉經 (Amenorrhea)

## 一句話總結

Goserelin 是一種 GnRH 受體促效劑，在香港尚未取得上市許可，但在國際上廣泛用於乳癌輔助治療、前列腺癌及子宮內膜異位症。TxGNN 模型預測它可能對**閉經 (Amenorrhea)** 有效（即治療性閉經誘導），目前有 **7 個臨床試驗**和 **19 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 乳癌輔助治療、前列腺癌、子宮內膜異位症（香港未上市，國際通用） |
| 預測新適應症 | 閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Goserelin 的核心機轉為 GnRH 受體促效劑：**持續給藥 → 垂體 GnRH 受體下調 → LH/FSH 分泌受抑制 → 卵巢雌激素合成降低 → 誘發可逆性閉經**。閉經本身即為 goserelin 的直接生理效果，因此本預測具備高度機轉合理性。

原適應症（荷爾蒙依賴性腫瘤、子宮內膜異位症）與本預測新適應症（閉經）在機轉上屬於同一條路徑的不同應用場景。治療閉經的兩條臨床路徑均有強力支持：其一為**卵巢功能抑制（Ovarian Suppression）**，作為乳癌輔助治療的核心機制之一；其二為**化療期間卵巢保護**，透過暫時性卵巢抑制，降低化療誘發性卵巢早衰（Premature Ovarian Insufficiency）風險，藉此保護生育功能。

此外，goserelin 亦被研究用於子宮腺肌症（誘導閉經以減輕症狀、保留生育能力）及因嚴重子宮出血需暫停月經的特殊臨床情境（如先天性再生不良性貧血所致的青春期月經過多）。上述適用場景均以同一 GnRH 促效劑機轉為基礎，臨床一致性高，支持此預測的合理性。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00427245](https://clinicaltrials.gov/study/NCT00427245) | Phase 3 | 完成 | 400 | OPTION 試驗：Goserelin 在化療期間給藥，評估是否能降低停經前乳癌患者早期停經發生率；為同類研究中樣本數最大的 Phase 3 試驗 |
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | 完成 | 257 | 化療 + Goserelin 對比單用化療，主要終點為卵巢衰竭（早期停經）率；研究 goserelin 是否能預防化療誘發的卵巢功能喪失 |
| [NCT02483767](https://clinicaltrials.gov/study/NCT02483767) | Phase 3 | 完成 | 98 | 前瞻性隨機對照試驗，停經前乳癌患者化療期間加入 GnRH 促效劑 goserelin，主要終點為卵巢功能保存 |
| [NCT01218581](https://clinicaltrials.gov/study/NCT01218581) | Phase 2/3 | 完成 | 32 | 芳香酶抑制劑 vs GnRH 促效劑用於子宮腺肌症管理，直接評估 goserelin 誘導閉經、保留生育能力之療效 |
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | 狀態不明 | 300 | Toremifene ± Goserelin 用於停經前荷爾蒙受體陽性乳癌（含或不含化療誘發閉經），化療誘發閉經為重要觀察終點 |
| [NCT03475758](https://clinicaltrials.gov/study/NCT03475758) | Phase 2 | 狀態不明 | 100 | Goserelin 用於含環磷醯胺化療期間的卵巢保護，主要終點為月經結果（menstruation outcome） |
| [NCT00488722](https://clinicaltrials.gov/study/NCT00488722) | 不適用 | 狀態不明 | 不詳 | Zoladex（goserelin）+ CEF 新輔助化療單臂研究；goserelin 可誘導可逆性閉經，臨床效果類似卵巢切除術 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Meta-analysis | Annals of Oncology | OPTION 試驗最終結果：GnRH 促效劑於化療期間給藥可顯著降低卵巢早衰（POI）發生率，支持 goserelin 的卵巢保護效益 |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Systematic Review | Breast Cancer Res Treat | LHRH 促效劑在早期乳癌大型臨床試驗回顧：goserelin 誘發可逆性卵巢切除，療效不亞於 CMF 化療 |
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | RCT | J Clin Oncol | IBCSG Trial VIII：比較化療、goserelin 或序貫治療對閉經、熱潮紅及生活品質的影響，分層分析顯示年齡差異 |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J Natl Cancer Inst | IBCSG Trial VIII：停經前淋巴結陰性乳癌患者，化療後序貫 goserelin vs 各單獨治療之隨機比較 |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | RCT | Cancer Res Treat | 卵巢切除（goserelin）改善無化療誘發閉經之 Stage II/III 荷爾蒙受體陽性乳癌患者存活率 |
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncol | ZEBRA 研究：goserelin vs CMF 用於停經前淋巴結陽性乳癌輔助治療，分析早期停經的長期影響 |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | RCT | Fertility and Sterility | Goserelin vs 低劑量口服避孕藥用於子宮內膜異位症骨盆疼痛，評估停藥後症狀復發率 |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Review | Br J Surgery | 停經前早期乳癌輔助治療中卵巢切除之回顧：比較各種誘導閉經方式的適應症與侵入性 |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Cohort | J Clin Oncol | 乳癌卵巢抑制治療中雌二醇監測必要性評估：探討 goserelin 誘導閉經的充分性確認方法 |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J R Army Med Corps | 閉經誘導方法回顧：goserelin 效果良好但成本較高；適合需要完全停經且不可接受突破性出血的特殊場景 |

---

## 香港上市資訊

Goserelin 目前在香港**未取得上市許可**，衛生署藥物許可證紀錄為 0 張。如需在香港使用，需透過特別途徑（如醫院管理局藥事委員會的特別申請）取得。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
多項已完成的 Phase 3 RCT（OPTION 試驗、NCT00068601、NCT02483767、IBCSG Trial VIII 等）直接驗證了 goserelin 誘導或調控閉經的臨床效益，TxGNN 預測分數高達 99.99%，證據等級達 L1；然而香港目前尚未核准 goserelin 上市，且安全性仿單與 MOA 資料存在缺口，需補齊後方可進入正式評估流程。

**若要推進需要：**
- 確認香港取得 goserelin 的合規途徑（未上市藥品之特別申請流程）
- 取得完整原廠仿單（警語、禁忌、DDI、不良反應資料）
- 補充 DrugBank MOA 詳細資料以完整機轉關聯性分析
- 明確臨床適應症定位：治療性閉經誘導（如子宮腺肌症）vs 化療期間卵巢保護（兩者機轉相同但監管路徑不同）
- 建立卵巢功能恢復監測計畫（基線與治療期間 E₂、LH、FSH 定期追蹤）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

