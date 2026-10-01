---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
---

# Bimatoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Bimatoprost：從青光眼／高眼壓到牙周相關畸形症候群

## 一句話總結

Bimatoprost 是前列腺醯胺（prostamide）F2α 類似物，原本用於青光眼與高眼壓治療。
TxGNN 模型預測它可能對**伴有牙齒及／或牙周成分的畸形症候群**有效，但目前**沒有臨床試驗**，檢索到的 **20 篇文獻**都是一般牙周炎文獻，沒有任何一篇提到 bimatoprost。這項預測僅來自圖譜模型。

> ⚠ 排名第 8 的預測適應症「禿髮 (alopecia)」有完整的臨床試驗，證據明顯強於本項，詳見文末補充章節。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 伴有牙齒及／或牙周成分的畸形症候群 (malformation syndrome with odontal and/or periodontal component) |
| TxGNN 預測分數 | 99.997% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，bimatoprost 是前列腺醯胺 F2α 類似物，用於降低眼壓，機轉上與牙周或牙齒發育畸形並無已知的直接關聯。

檢索到的文獻主要討論牙周炎的治療、微生物群與發炎機轉。這些論文沒有提到 bimatoprost，因此無法作為支持證據。

TxGNN 分數 (0.99997) 來自知識圖譜的網路鄰近性，不是臨床證據。目前找不到可信的機轉連結，這項預測應視為假說，不宜視為療效訊號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下文獻皆為牙周炎的一般性文獻，**均未提及 bimatoprost**。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | 系統性回顧 | Cochrane Database Syst Rev | 牙周炎治療對糖尿病患者血糖控制的影響 |
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | 指引 | J Clin Periodontol | EFP 第 IV 期牙周炎治療臨床實務指引 |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | Review | Diabetologia | 牙周炎與糖尿病的雙向關係 |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | Review | Periodontology 2000 | 牙周再生手術的併發症與處置失誤 |
| [39233377](https://pubmed.ncbi.nlm.nih.gov/39233377/) | 2024 | Review | Periodontology 2000 | 睡眠與牙周健康的關聯 |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | Review | J Dent Res | 牙齦纖維母細胞在牙周炎致病中的角色 |
| [29193334](https://pubmed.ncbi.nlm.nih.gov/29193334/) | 2018 | Review | Periodontology 2000 | 植體周圍與牙周邊緣軟組織的比較 |
| [12010523](https://pubmed.ncbi.nlm.nih.gov/12010523/) | 2002 | Review | J Clin Periodontol | 刮除與根面整平的實證觀點 |
| [38907216](https://pubmed.ncbi.nlm.nih.gov/38907216/) | 2024 | Review | J Nanobiotechnology | 以生醫材料調控巨噬細胞的牙周炎免疫治療 |
| [9495612](https://pubmed.ncbi.nlm.nih.gov/9495612/) | 1998 | 觀察性研究 | J Clin Periodontol | 齦下菌斑中的微生物複合體 |

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-60394 | LUMIGAN OPHTHALMIC SOLUTION 0.01% | ALLERGAN HONG KONG LIMITED |
| HK-68341 | ZIMED PRESERVATIVE FREE EYE DROPS SOLUTION 0.3MG/ML | DCH AURIGA (HONG KONG) LIMITED - UNIVERSAL DIVISION |
| HK-63183 | GANFORT PF EYE DROPS | ALLERGAN HONG KONG LIMITED |
| HK-56429 | GANFORT EYE DROPS | ALLERGAN HONG KONG LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 補充：證據較強的預測適應症——禿髮 (Alopecia)

在 10 個預測適應症中，只有**禿髮**有實質的臨床試驗（排名第 8，TxGNN 分數 99.993%，證據等級 L2）。

機轉上，prostamide/前列腺素訊號被認為可延長生長期 (anagen) 並刺激毛囊。這與 bimatoprost 已上市的睫毛增長作用一致。不過 MOA 欄位缺資料，這裡依據的是一般藥理知識。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | 完成 | 307 | Bimatoprost 對比 vehicle 與 minoxidil 5%，用於男性雄性禿 |
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | 完成 | 306 | Bimatoprost 對比 vehicle 與 minoxidil 2%，用於女性型禿髮 |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | 完成 | 244 | Bimatoprost 用於男性雄性禿的安全性與療效 |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | 完成 | 30 | 併用二氧化碳飛梭雷射治療斑禿，無法單獨評估藥物效果 |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | 完成 | 71 | 兒童睫毛稀疏，屬睫毛而非頭皮 |

- 上表只列出代表性試驗。另有多個 Phase 1 藥動與耐受性試驗，以及 1 個撤回（0 人）的試驗。
- 資料中**沒有 Phase 3 試驗**，各試驗的療效結果也未收錄。
- 斑禿方面，目前只有一項非隨機開放性研究（對比 clobetasol）與兒童個案報告。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 本項預測（牙周相關畸形症候群）沒有試驗、沒有直接文獻，也沒有可信的機轉連結，證據等級為 L5，僅為模型預測。
- 若要投入資源，禿髮是更值得評估的方向。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症
- 從 DrugBank 補上作用機轉 (MOA) 資料
- 取得並檢視禿髮 Phase 2 試驗（NCT01325337、NCT01325350、NCT01904721）的療效結果
- 釐清頭皮外用劑型與現有眼用製劑的給藥途徑差異

---

*本報告結果僅供研究參考，不構成醫療建議。預測適應症需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

