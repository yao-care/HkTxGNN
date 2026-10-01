---
layout: default
title: Cytarabine
parent: 中證據等級 (L3-L4)
nav_order: 235
evidence_level: L4
indication_count: 9
---

# Cytarabine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **9** 個
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

# Cytarabine：從血液腫瘤化療到小細胞肺癌

## 一句話總結

Cytarabine（阿糖胞苷）是一種抗代謝型的細胞毒性化療藥，文獻中主要用於白血病與淋巴瘤的化療方案，目前香港有 14 張許可證。
TxGNN 模型預測它可能對**小細胞肺癌 (Small Cell Lung Carcinoma)** 有效。
目前有 **3 個臨床試驗**和 **20 篇文獻**與此方向相關，但臨床試驗皆為間接證據，沒有任何一項直接檢驗 cytarabine 對小細胞肺癌的療效。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明適應症文字 |
| 預測新適應症 | 小細胞肺癌 (Small Cell Lung Carcinoma) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，cytarabine 是 S 期特異性的核苷類似物，會抑制 DNA 合成，因此對增生快速的腫瘤在機轉上具有合理性。小細胞肺癌正是高度增生的腫瘤。

不過，TxGNN 的高分（0.998）只是模型預測，不是臨床證據。實際檢視文獻後，支持程度有限：

- 1984 年的一項研究中，單用 cytarabine 治療 10 位已接受過多線治療的小細胞肺癌患者，沒有任何反應，且毒性嚴重。
- 另有研究把 cytarabine 併入 CAV 方案（25 位廣泛期患者），以及與 etoposide 併用於復發患者（17 位）。
- 其餘多為非小細胞肺癌的 Phase II 研究，或以腦膜轉移為主題的舊報告。

因此這個預測目前只能視為值得追蹤的假說。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | 提前終止 | 34 | 早期非小細胞肺癌術後輔助化療 vs 觀察。組織型不符，且未顯示 cytarabine 的角色 |
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | 完成 | 13 | 鞘內注射 pemetrexed 治療非小細胞肺癌軟腦膜轉移。藥物與組織型皆不同 |
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | 完成 | 34 | 鞘內 pemetrexed 併放療治療實體瘤軟腦膜轉移。非 cytarabine，也非小細胞肺癌 |

以上 3 個試驗的相關性評級皆為 C（間接）。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9363869](https://pubmed.ncbi.nlm.nih.gov/9363869/) | 1997 | RCT | J Clin Oncol | 局限期小細胞肺癌化放療加或不加 warfarin 的隨機試驗（CALGB）。摘要未提及 cytarabine |
| [2157307](https://pubmed.ncbi.nlm.nih.gov/2157307/) | 1990 | Phase II | Tumori | Cytarabine + cisplatin + vindesine 治療晚期非小細胞肺癌，32 人，28 位可評估者中 5 位有反應（18%） |
| [2156598](https://pubmed.ncbi.nlm.nih.gov/2156598/) | 1990 | Phase II | Cancer | 高劑量 cytarabine + cisplatin 治療未治療過的非小細胞肺癌，37 人，整體反應率 14%，32% 出現第四級骨髓抑制 |
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | 臨床研究 | Am J Clin Oncol | 連續輸注 ara-C：單用於 10 位已治療患者無反應且毒性嚴重；另 25 位廣泛期患者加入 CAV 方案 |
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | 臨床研究 | Am J Clin Oncol | Etoposide + 輸注 ara-C 治療 17 位難治性小細胞肺癌，其中 3 位於第一療程後因腫瘤進展死亡 |
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | 臨床研究 | Med Pediatr Oncol | 20 位未治療小細胞肺癌以 cyclophosphamide + Adriamycin + 皮下 cytarabine 併放療 |
| [6264785](https://pubmed.ncbi.nlm.nih.gov/6264785/) | 1981 | 病例系列 | Am J Med | 小細胞肺癌腦膜癌病；60 位接受強化化療者完全加部分緩解率 78%。摘要未指明 cytarabine 的貢獻 |
| [28223673](https://pubmed.ncbi.nlm.nih.gov/28223673/) | 2017 | 病例報告 | Gan To Kagaku Ryoho | 小細胞肺癌腦膜癌病以多專科整合治療獲得成效 |
| [11331076](https://pubmed.ncbi.nlm.nih.gov/11331076/) | 2001 | 前臨床 | Biochem Pharmacol | 對 daunorubicin 與 VM-26 產生抗藥的小細胞肺癌細胞株，對 gemcitabine 與 cytarabine 出現交叉敏感 |
| [2820740](https://pubmed.ncbi.nlm.nih.gov/2820740/) | 1987 | 先導研究 | Eur J Cancer Clin Oncol | Cisplatin + cytarabine 治療晚期非小細胞肺癌（摘要缺漏，僅有標題） |

---

## 香港上市資訊

香港共有 14 張許可證，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65688 | ACCORD CYTARABINE SOLUTION FOR INJECTION/INFUSION 100MG/1ML | 未載明 | 未載明 |
| HK-65687 | ACCORD CYTARABINE SOLUTION FOR INJECTION/INFUSION 1G/10ML | 未載明 | 未載明 |
| HK-65685 | ACCORD CYTARABINE SOLUTION FOR INJECTION/INFUSION 4G/40ML | 未載明 | 未載明 |
| HK-65684 | ACCORD CYTARABINE SOLUTION FOR INJECTION/INFUSION 5G/50ML | 未載明 | 未載明 |
| HK-36387 | CYTARABINE INJ 100MG/ML | 未載明 | 未載明 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（嘧啶類抗代謝藥／核苷類似物，S 期特異性） |
| 骨髓抑制風險 | 高。文獻中高劑量 cytarabine + cisplatin 有 32% 出現第四級骨髓抑制，另有研究描述毒性嚴重 |
| 致吐性分級 | 低至中度（依藥物類別與劑量判斷；文獻中噁心嘔吐為主要非血液毒性之一） |
| 監測項目 | CBC（含分類）、肝腎功能；文獻亦提及口腔黏膜炎 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

實際警語與劑量調整請參考原廠仿單。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗直接檢驗 cytarabine 對小細胞肺癌的療效。現有文獻多為 1980 至 1990 年代的舊研究，其中單藥於已治療患者無反應且毒性嚴重。
- 香港仿單的警語與禁忌症資料尚未取得，無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單（警語、禁忌症、適應症），完成安全性篩選
- 補充 cytarabine 的作用機轉資料（如 DrugBank）
- 檢索小細胞肺癌專屬的 cytarabine 臨床資料，特別是現代標準治療（platinum + etoposide 等）下的比較證據
- 其他預測適應症中，原發性肺淋巴瘤（L3）的機轉支持較強，因 cytarabine 本來就是淋巴瘤方案的骨幹，可列為優先追蹤項目，但目前也無針對該疾病的直接試驗

---

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

