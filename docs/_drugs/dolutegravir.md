---
layout: default
title: Dolutegravir
parent: 中證據等級 (L3-L4)
nav_order: 285
evidence_level: L4
indication_count: 3
---

# Dolutegravir
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Dolutegravir：從 HIV-1 感染到猴免疫缺陷病毒感染

## 一句話總結

Dolutegravir 是整合酶股轉移抑制劑（INSTI），在香港以 TIVICAY、DOVATO、TRIUMEQ 等製劑上市，用於 HIV 治療。
TxGNN 模型預測它可能對**猴免疫缺陷病毒感染 (Simian immunodeficiency virus infection)** 有效，
但這是動物模型疾病，目前僅有 **1 個間接相關的臨床試驗**和 **14 篇以前臨床為主的文獻**，屬於知識圖譜的推論結果，並非真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺漏（許可證未提供適應症文字；依藥理類別，為 HIV-1 感染） |
| 預測新適應症 | 猴免疫缺陷病毒感染 (Simian immunodeficiency virus infection) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中 MOA 欄位空白）。根據已知資訊，Dolutegravir 是 HIV-1 整合酶股轉移抑制劑，作用是阻止病毒 DNA 整合進宿主基因體。

SIV 的整合酶與 HIV-1 結構相近。HIV/SIV intasome 結構研究，以及獼猴的抗藥突變研究，都支持 Dolutegravir 對 SIV 有活性。因此模型把兩者連在一起，在機轉上說得通。

但要注意：SIV 是非人靈長類的動物模型疾病，沒有人類適應症。人類對應疾病 HIV-1 感染本來就已核准，原適應症欄位為空只是資料缺漏。因此這個預測比較像知識圖譜的產物，而不是真正的老藥新用機會。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | 未知 | 12 | Vedolizumab 併用抗反轉錄病毒療法，探討 HIV 感染者的持續病毒緩解；對象為人類 HIV，Dolutegravir 至多是背景療法，並未檢驗其對 SIV 的療效 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30381490](https://pubmed.ncbi.nlm.nih.gov/30381490/) | 2019 | 前臨床（獼猴） | Journal of Virology | Dolutegravir 單一療法用於 SIV 感染獼猴，篩選出多種抗藥突變，病毒學結果不一 |
| [36365101](https://pubmed.ncbi.nlm.nih.gov/36365101/) | 2022 | 前臨床（SIV 模型） | Pharmaceutics | 在 SIV 感染的非人靈長類模型中，驗證含 Dolutegravir 的長期抗病毒療法之藥理學特性 |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | 前臨床（抗藥性分析） | Journal of Virology | 描述 SIVmac239 對整合酶抑制劑的抗藥性圖譜，突變與 HIV 相似 |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | 前臨床（獼猴） | AIDS Res Hum Retroviruses | 比較兩種複方注射型抗反轉錄病毒療法在 SIV 感染獼猴的效果 |
| [28576126](https://pubmed.ncbi.nlm.nih.gov/28576126/) | 2017 | 病例報告 | Retrovirology | 圈養西非黑猩猩 SIVcpz 引起免疫缺陷，經治療後獲得改善 |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | 結構性回顧 | FEBS Journal | HIV/SIV intasome 結構，說明整合酶抑制劑的結合與病毒逃逸機轉 |
| [40093003](https://pubmed.ncbi.nlm.nih.gov/40093003/) | 2025 | 未分類 | Frontiers in Immunology | 獼猴開始 FTC + TDF + Dolutegravir 治療前後的細胞外自由水與神經纖維束變化 |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | 前臨床（腦部持續感染） | mBio | 即使有效的抗反轉錄病毒治療，慢病毒仍持續存在於腦部 |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | 未分類 | Journal of Virology | 將 HIV 整合酶抗藥突變導入 SIVmac239，評估對 INSTI 的敏感性 |
| [25583721](https://pubmed.ncbi.nlm.nih.gov/25583721/) | 2015 | 未分類 | Antimicrob Agents Chemother | 以嗜猴性 HIV 作為整合酶抑制劑抗藥性的研究模型 |

（另有 4 篇相關性較低的文獻未列出，含流行病學、Wnt 通路、p38 MAPK 及脂肪組織副作用研究。）

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63516 | TIVICAY TABLETS 50MG | 錠劑 | 資料未提供 |
| HK-66511 | DOVATO TABLETS | 錠劑 | 資料未提供 |
| HK-64012 | TRIUMEQ TABLETS | 錠劑 | 資料未提供 |

三張許可證的持有廠商皆為 GlaxoSmithKline Limited。

---

## 安全性考量

安全性資訊請參考原廠仿單。（香港衛生署仿單的警語與禁忌資料尚未取得，DDI 查詢也無結果。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- SIV 是動物模型疾病，證據僅限前臨床，沒有人類族群；人類對應疾病 HIV-1 已有核准適應症，這是知識圖譜的假象，不是真正的老藥新用機會。
- 香港仿單的安全性資料缺漏，屬阻擋性資料缺口，尚無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊原適應症、警語與禁忌症
- 從 DrugBank 補齊作用機轉（MOA）
- 建議將此預測標為「動物模型／人類已核准類似疾病」，不列入人類新適應症清單；若有獸醫用途興趣，需另建獸醫證據流程

---

### 其他預測適應症（供參考）

| 排名 | 預測疾病 | TxGNN 分數 | 證據等級 | 說明 |
|------|---------|-----------|---------|------|
| 2 | 貓後天免疫缺陷症候群 (Feline AIDS) | 99.85% | L4 | 5 個 HIV-1 試驗屬人類疾病的間接證據，僅 1 篇貓 cART 研究（2023）使用 Dolutegravir 複方；為獸醫適應症 |
| 3 | 伴隨共濟失調步態、無語言及皮質白質減少的神經發育障礙 | 99.80% | L5 | 無臨床試驗與文獻，找不到機轉關聯，僅為模型預測 |

---

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

