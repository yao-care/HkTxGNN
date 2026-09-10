---
layout: default
title: Maraviroc
parent: 中證據等級 (L3-L4)
nav_order: 474
evidence_level: L4
indication_count: 10
---

# Maraviroc
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

# Maraviroc：從 HIV-1 感染治療到 HER2 陽性乳癌抗藥機轉

## 一句話總結

Maraviroc 是 CCR5 拮抗劑，臨床上作為抗反轉錄病毒藥物用於 HIV-1 感染治療（此藥未在本地上市，正式適應症登記資料缺失）。TxGNN 針對此藥產出 10 個候選新適應症，其中 9 個完全無臨床試驗或文獻支持；唯一有機轉文獻佐證的是 **HER2 陽性乳癌（HER2 Positive Breast Carcinoma）**——文獻顯示 CCL5-CCR5 訊息軸可能介導 trastuzumab 抗藥性，理論上 CCR5 阻斷劑或可逆轉此機轉，但僅為體外研究，證據等級 L4，尚無臨床或動物驗證。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未列於當地許可證資料（藥物未上市）；依文獻脈絡為 HIV-1 感染／抗反轉錄病毒治療 |
| 預測新適應症 | HER2 陽性乳癌（HER2 Positive Breast Carcinoma）—10 個候選中唯一具機轉文獻支持者 |
| TxGNN 預測分數 | 99.22% |
| 證據等級 | L4 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

DrugBank 官方作用機轉欄位為缺失資料，但依據證據包中文獻脈絡，Maraviroc 屬 CCR5 拮抗劑，透過阻斷 CCR5 受體抑制 HIV 病毒進入 T 細胞，原用於 HIV-1 感染的抗反轉錄病毒治療。

HER2 陽性乳癌與 HIV 感染在臨床上並無直接關聯，但兩者可能透過同一趨化因子受體共享機轉：文獻（Zazo et al., 2020, *Molecular Cancer Therapeutics*）指出，HER2 陽性乳癌細胞可透過自泌性 CCL5 活化 CCR5，進而啟動 ERK 訊息路徑，介導對 trastuzumab 的原發性或後天抗藥性。

理論上，Maraviroc 作為 CCR5 拮抗劑可能阻斷此 CCL5-CCR5-ERK 軸，逆轉部分 trastuzumab 抗藥腫瘤的敏感性。然而，此推論目前僅建立在體外機轉研究上，尚無動物模型或臨床試驗驗證 Maraviroc 本身在乳癌中的實際療效。

其餘 9 個 TxGNN 預測適應症（如 multiple endocrine neoplasia、acne、pediatric SLE 等）經逐一查證 ClinicalTrials.gov、ICTRP、PubMed 後均無相關試驗或文獻，機轉合理性也普遍薄弱，證據等級為 L5，純屬模型分數，暫不具評估價值。

## 臨床試驗證據

目前無相關臨床試驗登記（HER2 陽性乳癌候選及其餘 9 個候選適應症皆查無 ClinicalTrials.gov 或 ICTRP 登記試驗）。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32404410](https://pubmed.ncbi.nlm.nih.gov/32404410/) | 2020 | Basic/Mechanistic | Molecular Cancer Therapeutics | HER2 陽性乳癌細胞透過自泌性 CCL5-CCR5 軸活化 ERK 路徑，介導 trastuzumab 抗藥性 |

其餘候選適應症中另有 5 篇文獻（PMID 37006247、21671545、26960018、25397464、25397464），但均為 HIV 抗反轉錄病毒治療的背景性綜述或安全性描述，未直接評估 Maraviroc 對該等適應症的療效，相關性較弱，故未列入本次主要證據。

## 香港上市資訊

Maraviroc 目前未在香港上市，無許可證登記資料（許可證總數：0）。

## 安全性考量

安全性資訊請參考原廠仿單。（本評估包中警語、禁忌症與藥物交互作用資料均缺失，其中仿單警語/禁忌屬於 Blocking 等級資料缺口，需取得後才能進入 S1 安全性初評。）

## 結論與下一步

**決策：Hold**

**理由：**
- 10 個 TxGNN 候選適應症中，9 個完全無臨床試驗或文獻證據，證據等級皆為 L5；HER2 陽性乳癌雖有機轉文獻支持，但仍僅為體外研究（L4），無動物或臨床數據佐證。
- 藥物本身未在本地上市、官方 MOA 與仿單安全性資料皆缺失，尚不具備進入下一階段評估的基本條件。

**若要推進需要：**
- 補齊 TFDA／原廠仿單警語與禁忌資料（Blocking 缺口，須完成才能進行 S1 安全性初評）
- 透過 DrugBank API 取得正式作用機轉（MOA）資料
- 若優先推進 HER2 陽性乳癌方向：需體外/動物模型驗證 Maraviroc 阻斷 CCR5 對 trastuzumab 抗藥性腫瘤的實際逆轉效果，作為申請臨床試驗前的前臨床證據
- 其餘 9 個候選適應症證據不足，除非後續出現新文獻或試驗登記，暫不建議投入資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

