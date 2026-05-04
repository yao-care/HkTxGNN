---
layout: default
title: Atorvastatin
parent: 高證據等級 (L1-L2)
nav_order: 69
evidence_level: L1
indication_count: 6
---

# Atorvastatin
{: .fs-9 }

證據等級: **L1** | 預測適應症: **6** 個
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

# Atorvastatin：從高膽固醇血症到家族性高膽固醇血症

## 一句話總結

Atorvastatin（阿托伐他汀）是全球廣泛使用的 HMG-CoA 還原酶抑制劑（他汀類藥物），主要用於原發性高膽固醇血症與心血管風險管理。
TxGNN 模型預測它可能對**家族性高膽固醇血症 (Familial Hypercholesterolemia, FH)** 尤其有效，
目前有 **35 個臨床試驗**和 **19 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 原發性高膽固醇血症、混合型血脂異常（全球通用適應症） |
| 預測新適應症 | 家族性高膽固醇血症 (Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.42% |
| 證據等級 | L1 |
| 香港上市 | ✗ 香港藥物資料庫未有登記 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Atorvastatin 是第二代合成他汀類藥物，透過競爭性抑制 HMG-CoA 還原酶（膽固醇合成的限速酶），阻斷肝臟內甲羥戊酸（mevalonate）路徑，降低細胞內膽固醇的從頭合成。此機轉代償性上調肝臟 LDL 受體（LDLR）的表達密度，進而加速血液中 LDL-C 的清除，同時具延長半衰期（20–30 小時）所帶來的持久 HMG-CoA 抑制效果。

家族性高膽固醇血症（FH）的核心致病機轉恰好是 LDLR 功能缺陷（雜合子或純合子突變）、或 PCSK9 過度活化導致 LDLR 加速降解，造成血漿 LDL-C 嚴重且持續的升高。Atorvastatin 藉由上調殘存 LDLR 活性（在雜合子 FH 患者效果尤為顯著），直接針對 FH 的核心病理生理機轉，是 FH 治療中最重要的藥理基礎之一。

事實上，Atorvastatin 在全球多個國家（美國、歐盟、日本、台灣等）早已取得 FH 相關適應症核准，並在 AACE/ACE、ACC/AHA、EAS 等主要國際心臟學及內分泌學指引中列為 FH 的一線治療藥物。TxGNN 模型的預測與現有臨床實踐高度吻合，同時呼應了多項大型 Phase 3 RCT 的實證結果。本次評估中「香港未上市」的狀態可能反映資料庫收錄範圍的限制，而非藥物的實際可及性。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | 完成 | 486 | 雙盲 RCT，alirocumab 在 heFH 患者（穩定 atorvastatin 為背景治療）中降低 LDL-C 的療效與安全性評估 |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Phase 3 | 完成 | 355 | 以 atorvastatin 為基礎，比較加入 alirocumab、加入 ezetimibe、加大劑量及換用 rosuvastatin 四種策略，確立 atorvastatin 在 heFH 的標準治療地位 |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | 完成 | 249 | 雙盲 RCT，評估 alirocumab 在 heFH 患者（現行脂質修飾治療基礎）中改善 LDL-C 控制的療效 |
| [NCT03867318](https://clinicaltrials.gov/study/NCT03867318) | Phase 3 | 完成 | 621 | ezetimibe 10mg 加入 atorvastatin 治療 heFH 或高心血管風險高膽固醇血症患者的療效與安全性 |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | 完成 | 44 | ezetimibe 加入 atorvastatin 或 simvastatin 治療 hoFH 的 24 個月長期安全性與耐受性研究 |
| [NCT01507831](https://clinicaltrials.gov/study/NCT01507831) | Phase 3 | 完成 | 2341 | alirocumab 在高心血管風險高膽固醇血症患者（背景為 atorvastatin）的長期安全性與降 LDL-C 效果，樣本量最大 |
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Phase 3 | 完成 | 272 | 3 年開放性研究，描述 atorvastatin 在 heFH 兒童及青少年的長期療效、生長發育及安全性 |
| [NCT00134511](https://clinicaltrials.gov/study/NCT00134511) | Phase 3 | 完成 | 30 | torcetrapib/atorvastatin 複方在 hoFH 患者中的強制滴定療效評估（torcetrapib 後因其他安全原因終止） |
| [NCT00145431](https://clinicaltrials.gov/study/NCT00145431) | Phase 3 | 提前終止 | 41 | 多中心雙盲交叉設計，評估 torcetrapib/atorvastatin 在 III 型高脂蛋白血症（家族性異常 β 脂蛋白血症）的療效 |
| [NCT01107743](https://clinicaltrials.gov/study/NCT01107743) | N/A | 完成 | 1291 | Caduet（amlodipine/atorvastatin 複方）上市後安全性與療效監測，大樣本真實世界觀察 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | 臨床指引 | Endocrine Practice | AACE/ACE 血脂異常管理與心血管預防指引，確立 atorvastatin 在 FH 一線治療的核心地位 |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | 世代研究 | JACC | 大型世代研究，量化 statin 治療對 heFH 患者冠心病事件及全因死亡率的影響 |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | 回顧文獻 | Curr Atherosclerosis Reports | 回顧 hoFH 的新型降 LDL 藥物療法，包含 statin 聯合治療最新進展 |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | 臨床研究回顧 | Ann Pharmacother | 早期回顧 atorvastatin 在原發性高膽固醇血症與混合型血脂異常的療效與安全性 |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | 比較研究 | Nutr Metab Cardiovasc Dis | atorvastatin vs simvastatin 在 heFH 患者達到 NCEP 指引 LDL-C 目標的頭對頭比較 |
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | 臨床研究 | J Clin Lipidology | 3 年長期研究評估 atorvastatin 在 heFH 兒童及青少年（含 6 歲以上）的療效與安全性 |
| [22957727](https://pubmed.ncbi.nlm.nih.gov/22957727/) | 2013 | 臨床研究 | Echocardiography | atorvastatin 顯著改善 FH 患者心肌及周邊血流灌注，證實其多效性心血管保護作用 |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | 基因流行病學 | Pharmacogenomics J | 結合 FH 基因診斷與 statin 藥物基因組學策略，探討基因型引導的個人化 statin 處方 |
| [26988948](https://pubmed.ncbi.nlm.nih.gov/26988948/) | 2016 | 綜述 | JACC | 改善 FH 患者長期監測與照護品質的建議，涵蓋 statin 治療策略優化 |
| [10582478](https://pubmed.ncbi.nlm.nih.gov/10582478/) | 1999 | 藥物綜述 | Rev Med Bruxelles | Atorvastatin 作用機轉、藥效學（HMG-CoA 還原酶抑制、LDL-C 降低）與臨床療效系統回顧 |

---

## 香港上市資訊

Atorvastatin 目前在香港衛生署藥物資料庫中**未有登記**，許可證數為 0。

> **注意**：Atorvastatin（代表品牌 Lipitor®）是全球銷售量最大的處方藥之一，在美國（FDA）、歐盟（EMA）、中國大陸、台灣（TFDA）等地均已上市，並持有高膽固醇血症及家族性高膽固醇血症等適應症核准。香港藥物資料庫未收錄可能反映資料庫收錄範圍或分類方式的限制，建議進一步向衛生署確認 Lipitor® 及其學名藥的實際香港上市狀態。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Atorvastatin 用於家族性高膽固醇血症有多項大型 Phase 3 RCT 支持（直接以 atorvastatin 為干預或標準背景治療，合計樣本總數超過 5,000 人），並已納入多個國際指引作為一線建議，證據等級達 L1，推進基礎充分。主要待釐清事項為香港本地許可狀態，以及正式安全性資料的建立。

**若要推進需要：**
- 向香港衛生署確認 Atorvastatin（Lipitor® 及學名藥）在港的實際上市許可狀態
- 取得完整香港仿單，建立正式安全性資料（警語、禁忌症、藥物交互作用，特別是與 CYP3A4 抑制劑的交互作用）
- 評估與香港本地臨床指引的一致性（如 Hospital Authority 血脂管理建議）
- 針對特殊族群（FH 兒童、育齡婦女、慢性腎病患者）制定個人化安全性監測計畫
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

