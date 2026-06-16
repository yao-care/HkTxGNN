---
layout: default
title: Clavulanic Acid
parent: 高證據等級 (L1-L2)
nav_order: 177
evidence_level: L2
indication_count: 10
---

# Clavulanic Acid
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

# Clavulanic Acid：從 β-Lactamase 抑制劑到淋球菌性尿道炎

---

## 一句話總結

Clavulanic Acid 是一種 β-lactamase 抑制劑，臨床上幾乎不單獨使用，而是與 amoxicillin 複方（商品名 Augmentin）搭配，用於克服細菌對青黴素的耐藥性。
TxGNN 模型預測它可能對**淋球菌性尿道炎（Gonococcal Urethritis）** 有效，
目前有 **0 個臨床試驗**和 **14 篇文獻**支持這個方向，其中包含 3 篇隨機對照試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無許可證資料（香港未上市） |
| 預測新適應症 | 淋球菌性尿道炎（Gonococcal Urethritis） |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Clavulanic Acid 的作用機轉為不可逆地抑制細菌所產生的 β-lactamase 酶。當 Neisseria gonorrhoeae（淋球菌）產生 penicillinase（PPNG 株）時，青黴素類抗生素即失效；Clavulanic Acid 能「保護」amoxicillin 不被水解，使其恢復對 PPNG 的殺菌能力。這個機轉在 1980 年代 PPNG 流行高峰時期尤為關鍵，Augmentin 複方因此被系統性地研究用於淋病治療。

淋球菌性尿道炎本身是 Neisseria gonorrhoeae 感染泌尿道的直接表現，傳統上以青黴素治療。Clavulanic Acid 的引入解決了 β-lactamase 介導的耐藥性問題，使 amoxicillin 的療效得以恢復，機轉關聯性清晰且直接。

需要特別注意的是：現代臨床指引（WHO、CDC）已轉向 ceftriaxone 肌肉注射作為淋病首選治療，主要原因是多重耐藥性淋球菌持續演化，且對 Augmentin 方案的耐藥性報告增加。因此，本預測的臨床意義須在當代耐藥性流行病學背景下重新評估。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [4007860](https://pubmed.ncbi.nlm.nih.gov/4007860/) | 1985 | Dose Comparison RCT | Genitourinary Medicine | Amoxicillin 3g + Clavulanic Acid 125mg 單劑口服治療非複雜性淋病，100 例中 97 例治癒（97%），含 PPNG 株治癒率 85% |
| [6365235](https://pubmed.ncbi.nlm.nih.gov/6365235/) | 1984 | Comparative RCT | Br J Venereal Diseases | 121 名男性非複雜性淋球菌尿道炎，Augmentin 單劑口服 vs 普魯卡因青黴素肌注，Augmentin 組治癒率 90.6%，優於對照組 73.7% |
| [3721514](https://pubmed.ncbi.nlm.nih.gov/3721514/) | 1986 | 3-arm Comparative Trial | Genitourinary Medicine | 三種青黴素方案比較，Augmentin 3.25g 口服 + probenecid 對 PPNG 株治癒率達 100% |
| [6757686](https://pubmed.ncbi.nlm.nih.gov/6757686/) | 1982 | Clinical Trial | Medical Journal of Malaysia | 男性淋球菌尿道炎單劑口服 amoxycillin + clavulanic acid 治療研究 |
| [3533755](https://pubmed.ncbi.nlm.nih.gov/3533755/) | 1986 | Comparative Trial | Genitourinary Medicine | 500 例非複雜性淋病隨機研究，比較 cefuroxime axetil 與 Amoxicillin + Clavulanic Acid（各含 250+ 名受試者），評估泌尿生殖道及直腸淋病療效 |
| [3004176](https://pubmed.ncbi.nlm.nih.gov/3004176/) | 1985 | Clinical Trial | African J Medicine | 奈及利亞 PPNG 盛行率約 80% 的環境，Augmentin 兩種劑型單劑治療淋球菌尿道炎，評估不同配方療效 |
| [3147528](https://pubmed.ncbi.nlm.nih.gov/3147528/) | 1988 | Clinical Study | Sexually Transmitted Diseases | 比較 spectinomycin、ceftriaxone 及 clavulanic acid 強化青黴素方案治療 PPNG 感染，分析各方案對不同解剖部位及費用之考量 |
| [6428699](https://pubmed.ncbi.nlm.nih.gov/6428699/) | 1984 | Clinical Trial | Br J Venereal Diseases | 192 名急性淋球菌尿道炎男性，Augmentin 兩劑口服（間隔 4 小時）治癒率 95.9%，優於 kanamycin 87.4% |
| [7958383](https://pubmed.ncbi.nlm.nih.gov/7958383/) | 1994 | Open Study | J International Medical Research | 55 名急性淋病患者接受普魯卡因青黴素 + Clavulanate-Augmentin 口服組合，96.4% 有膿性分泌物，92.5% 為青黴素敏感株 |
| [19544099](https://pubmed.ncbi.nlm.nih.gov/19544099/) | 2009 | Retrospective Review | Rev Esp Quimioter | 馬德里市中心 3 年尿道炎回顧分析，研究致病微生物流行率及趨勢 |

---

## 香港上市資訊

Clavulanic Acid（單一成分）在香港目前**未上市**，無相關藥品許可證登記。

> 注意：Clavulanic Acid 幾乎不作為單一成分上市，通常以 Amoxicillin/Clavulanate 複方（Augmentin）形式流通。香港市場上 Augmentin 複方製劑由 amoxicillin 取得許可，Clavulanic Acid 為複方成分之一。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
文獻證據包含 3 篇隨機對照試驗（1982–1986 年），系統性評估了 Augmentin（含 Clavulanic Acid）治療淋球菌性尿道炎的療效，治癒率普遍達 90% 以上，機轉明確（抑制 PPNG β-lactamase，恢復 amoxicillin 殺菌力）。然而，現代 STI 指引已優先推薦 ceftriaxone IM，耐藥性情境已顯著改變，本研究方向具有歷史臨床意義，但直接現代應用需要審慎評估當代耐藥性數據。

**若要推進需要：**
- 調查當前香港及目標市場 Neisseria gonorrhoeae β-lactamase 盛行率與耐藥性譜（含對 amoxicillin/clavulanate 的 MIC 分布）
- 取得詳細安全性資料：查詢 Augmentin 複方仿單的警語、禁忌症及藥物交互作用
- 與香港性病防治指引（如衛生防護中心建議）對照，確認 Augmentin 是否仍在替代方案清單中
- 考慮以複方（Amoxicillin/Clavulanate）而非單一成分為研究主體，重新設計適應症拓展框架
- 補充 DrugBank 作用機轉詳細資料（MOA 目前缺失）

---

> ⚠️ **免責聲明**：本報告僅供研究參考，不構成醫療建議。所有老藥新用候選均需經過嚴格臨床驗證方可應用於實際診療。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

