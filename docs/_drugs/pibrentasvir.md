---
layout: default
title: Pibrentasvir
parent: 僅模型預測 (L5)
nav_order: 681
evidence_level: L5
indication_count: 5
---

# Pibrentasvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Pibrentasvir：從 C 型肝炎到 B 型肝炎

## 一句話總結

Pibrentasvir 是 HCV NS5A 抑制劑，與 glecaprevir 組成複方（香港商品名 MAVIRET），原本用於 C 型肝炎。
TxGNN 模型預測它可能對 **B 型肝炎病毒感染 (Hepatitis B virus infection)** 有效，但檢索到的 **14 個臨床試驗**和 **20 篇文獻**全部是 C 肝研究，沒有任何 B 肝療效的直接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | C 型肝炎（許可證未載明適應症文字，依機轉資料與試驗內容判斷） |
| 預測新適應症 | B 型肝炎病毒感染 (Hepatitis B virus infection) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5（證據包標示 L4，但未見 HBV 相關的前臨床或機轉研究，故判為僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前**沒有支持這個預測的機轉依據**。Pibrentasvir 抑制的是 HCV 的 NS5A 蛋白，作用位點是 C 肝病毒獨有的。

HBV 沒有 NS5A 同源蛋白，它是透過反轉錄酶與 cccDNA 途徑複製，因此 pibrentasvir 不可能直接抑制 HBV。TxGNN 分數很高，較可能反映的是知識圖譜中病毒性肝炎節點彼此距離相近，而不是真實的藥理關聯。

另外要特別注意：HBV 再活化是 DAA 類藥物在 HCV/HBV 共感染患者身上已知的類別風險。因此 HBV 與這個藥的關聯，更像安全性議題，而不是治療訊號。

## 臨床試驗證據

以下試驗均為 pibrentasvir（ABT-530）用於 C 肝的研究，**沒有任何一項以 HBV 為終點**。證據包對其中數項的 HBV 相關性評為 C 級（不相關），推測是關鍵字重疊造成配對。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01995071](https://clinicaltrials.gov/study/NCT01995071) | Phase 2 | 完成 | 89 | 基因型 1 C 肝，ABT-493/ABT-530 多劑量的安全性與抗病毒效果（C 級） |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | 完成 | 506 | ENDURANCE-3：基因型 3 C 肝，對比 sofosbuvir + daclatasvir（C 級） |
| [NCT02243293](https://clinicaltrials.gov/study/NCT02243293) | Phase 2/3 | 完成 | 694 | SURVEYOR-II：基因型 2、3、4、5、6 C 肝，合併或不合併 ribavirin（C 級） |
| [NCT02640482](https://clinicaltrials.gov/study/NCT02640482) | Phase 3 | 完成 | 304 | ENDURANCE-2：基因型 2 C 肝，安慰劑對照（C 級） |
| [NCT02446717](https://clinicaltrials.gov/study/NCT02446717) | Phase 2/3 | 完成 | 141 | 先前 DAA 治療失敗的 C 肝患者再治療 |
| [NCT02243280](https://clinicaltrials.gov/study/NCT02243280) | Phase 2 | 完成 | 174 | SURVEYOR-I：基因型 1、4、5、6 C 肝（C 級） |
| [NCT02707952](https://clinicaltrials.gov/study/NCT02707952) | Phase 3 | 完成 | 295 | CERTAIN-1：日本成人 C 肝 |
| [NCT02723084](https://clinicaltrials.gov/study/NCT02723084) | Phase 3 | 完成 | 136 | CERTAIN-2：日本基因型 2 C 肝，對比 sofosbuvir + ribavirin |
| [NCT03219216](https://clinicaltrials.gov/study/NCT03219216) | Phase 3 | 完成 | 100 | 巴西初治 C 肝，8 或 12 週療程（C 級） |
| [NCT02441283](https://clinicaltrials.gov/study/NCT02441283) | Phase 2/3 | 完成 | 384 | 長期追蹤：治療反應持久性與抗藥性 |

## 文獻證據

沒有 RCT，也沒有任何以 HBV 治療為主題的研究。以下依類型與相關性挑選。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) | 2018 | Review | Lancet Infect Dis | C 肝治療後接種 B 肝疫苗的必要性 |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | C 肝 DAA 藥動學與藥效學 2019 更新 |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | DAA 治療失敗的 C 肝患者再治療 |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | 兒童病毒性肝炎治療進展；指出 HBV 治療仍遠未達治癒 |
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Cohort | J Viral Hepat | 台灣 108 位 CKD 4/5 期 C 肝患者使用 GLE/PIB 的真實世界療效與安全性 |
| [37286314](https://pubmed.ncbi.nlm.nih.gov/37286314/) | 2023 | 回溯性研究 | BMJ Open | 台灣南部監獄 C 肝患者治療成效與副作用 |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | 回溯性研究 | Klin Mikrobiol Infekc Lek | 捷克 Ostrava 兒童 B 肝與 C 肝的抗病毒治療 |
| [31129632](https://pubmed.ncbi.nlm.nih.gov/31129632/) | 2019 | Case report | BMJ Case Rep | GLE/PIB 相關急性肝損傷（無 HBV 共感染） |
| [34344581](https://pubmed.ncbi.nlm.nih.gov/34344581/) | 2021 | Case report | J Infect Chemother | GLE/PIB 治療 daratumumab 方案誘發的 C 肝急性惡化 |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | 會議報告 | AIDS Rev | 2017 國際病毒性肝炎大會報告 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-65653 | MAVIRET TABLETS | ABBVIE LIMITED |

## 安全性考量

- **HBV 再活化風險**：DAA 治療 HCV/HBV 共感染患者時，已知有 HBV 再活化的類別風險。若考慮任何與 HBV 相關的用途，必須先處理這點。
- **肝損傷個案**：有 GLE/PIB 相關急性肝損傷的病例報告（PMID 31129632）。

其他警語、禁忌症與藥物交互作用資料（DDI 查詢無結果），請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測缺乏機轉依據：NS5A 是 HCV 特有的靶點，HBV 沒有對應蛋白。
- 所有檢索到的試驗與文獻都是 C 肝研究，沒有一項直接測試 pibrentasvir 對 HBV 的效果。
- HBV 再活化是已知風險，不應作為治療方向推進。
- 同一份分析中的其他預測（HIV、E 型肝炎、A 型肝炎、動物病毒性肝炎）同樣缺乏機轉與臨床證據，並不能支持這個藥物轉用。

**若要推進需要：**
- 體外（in vitro）HBV 複製抑制實驗，證明 pibrentasvir 對 HBV 有活性。
- 若體外有活性，需有明確的作用機轉假說。
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選。
- 評估 HBV 再活化風險及 HBV 篩檢與監測方案。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

