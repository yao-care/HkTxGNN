---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 267
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# Diazepam：從原適應症（資料未提供）到失眠

## 一句話總結

Diazepam 是苯二氮平類（benzodiazepine）藥物，在香港有 20 張許可證。本次提供的資料未載明其原適應症。
TxGNN 模型預測它可能對**失眠 (Insomnia)** 有效，但目前的 20 個試驗與 15 篇文獻，**沒有任何一項直接檢驗 diazepam 治療失眠的療效**。多數證據談的是安眠藥停藥、依賴與風險，屬於安全性背景。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 失眠 (Insomnia) |
| TxGNN 預測分數 | 99.9997% |
| 證據等級 | L3（僅有綜述與觀察性研究，無 diazepam 治療失眠的已完成 RCT） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Diazepam 是 GABA-A 受體的正向異位調節劑（PAM）。它增強抑制性神經傳導，理論上可帶來鎮靜並縮短入睡時間，這是模型預測合理的機轉基礎。不過本次資料缺少 DrugBank 的作用機轉欄位，以上是依預測理由推論，並非原廠資料。

苯二氮平類藥物早已用於失眠，例如 1981 年有一項雙盲研究比較 lormetazepam 與 diazepam 用於 100 位失眠門診病人。但 TxGNN 分數只是圖譜關聯，不等於臨床證據。原適應症資料缺漏，也無法確認這個預測與現有核准適應症的重疊程度。

另一項限制是安全性。長期使用會有耐受、依賴、次日功能受損與戒斷問題。臨床試驗中最多的正是安眠藥減量與停藥研究，也反映了這些風險。

## 臨床試驗證據

以下試驗都不是在檢驗 diazepam 治療失眠的療效，主要與安眠藥或苯二氮平類的停藥、依賴及風險有關。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Phase 2 | 完成 | 74 | 探討減量速度與個人特質對失眠患者停用安眠藥的影響 |
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Phase 3 | 進行中（不再招募） | 260 | 盲法減量加 CBT-I 對比開放標籤減量，評估停藥率 |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | 觀察性 | 未知 | 1400 | 台灣老年人安眠藥的風險與效益世代研究 |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | 完成 | 188 | 以非藥物策略協助老年人停用安眠藥 |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | N/A | 完成 | 128 | 遠距接受與承諾治療（ACT）對苯二氮平戒斷的效果 |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Phase 4 | 完成 | 17 | 以 ramelteon 輔助苯二氮平類與非苯二氮平類安眠藥減量，樣本極小 |
| [NCT05935553](https://clinicaltrials.gov/study/NCT05935553) | Phase 2/3 | 招募中 | 93 | 以 baclofen 輔助苯二氮平依賴者減量 |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | 提前終止 | 2 | Gabapentin 治療苯二氮平依賴，僅收 2 人 |
| [NCT02281175](https://clinicaltrials.gov/study/NCT02281175) | N/A | 完成 | 114 | PASSE-65+ 心理社會介入，協助老年人逐步減用苯二氮平 |
| [NCT04364321](https://clinicaltrials.gov/study/NCT04364321) | N/A | 未知 | 74 | Clonazepam 單劑對比間歇性 diazepam 預防復發性熱性痙攣（適應症不同） |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | 雙盲比較試驗 | J Int Med Res | 100 位失眠門診病人，lormetazepam 1 mg 在入睡時間等指標優於 diazepam 5 mg（7 天） |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT（依標題判斷，設計未確認） | JAMA Intern Med | 遮蔽式減量加行為介入，用於停用苯二氮平受體促效劑類安眠藥 |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | 統合分析 | Acta Pharm | 評估鎮靜藥用於老年慢性病患者的劑量、結果與不良反應 |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorg Chem | GABA-A 受體調節劑的臨床應用，diazepam 為代表性正向異位調節劑，並伴隨鎮靜等副作用 |
| [7595266](https://pubmed.ncbi.nlm.nih.gov/7595266/) | 1995 | 系統性回顧 | J Fam Pract | 社區老年人使用苯二氮平治療失眠的效益與風險，缺乏長期療效研究 |
| [7525193](https://pubmed.ncbi.nlm.nih.gov/7525193/) | 1994 | Review（指引） | Drugs | 苯二氮平合理使用指引，作為安眠藥只建議短期使用 |
| [40570297](https://pubmed.ncbi.nlm.nih.gov/40570297/) | 2025 | 世代研究 | Sleep | 長期使用苯二氮平類影響老年慢性失眠者的睡眠結構與腦波 |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | 臨床證據加機轉研究 | Cell Mol Biol Lett | 長期使用苯二氮平類及 Z-drugs 與乳癌風險上升有關 |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | 前臨床（動物） | Nat Neurosci | 長期 diazepam 經 TSPO 增強微膠細胞吞噬突觸，造成小鼠認知受損 |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Review | Drugs | Triazolam 用於失眠的藥理與療效（非 diazepam，可作類別參考） |

## 香港上市資訊

香港共登記 20 張許可證，以下列出 5 張。資料未提供劑型與核准適應症欄位，劑型由品名推斷。

| 許可證號 | 品名 | 劑型（由品名判斷） | 製造商 |
|---------|------|------|--------|
| HK-11468 | DIAZEPAM TAB 2MG | 錠劑 | Unicorn Laboratories |
| HK-32730 | KRATIUM 10 TAB 10MG | 錠劑 | Star Medical Supplies |
| HK-45358 | DIAZEPAM INJ 5MG/ML | 注射劑 | Luen Cheong Hong |
| HK-11508 | DIAZEPAM TAB 1MG | 錠劑 | Unicorn Laboratories |
| HK-38493 | SEDAPAM-5 TAB 5MG | 錠劑 | Synco (H.K.) |

## 安全性考量

安全性資訊請參考原廠仿單。

本次資料缺少香港衛生署仿單的警語與禁忌，藥物交互作用查詢也無結果。從文獻可見的類別風險包括：

- 長期使用可能造成依賴、耐受與戒斷。
- 長期使用可能造成認知受損，有動物實驗證據（PMID 35228700）。
- 長期使用可能增加乳癌風險，屬相關性研究（PMID 40583063）。
- Diazepam 本身有濫用與誤用風險（見「barbiturate abuse」預測項下的文獻）。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何試驗或文獻直接證明 diazepam 治療失眠的療效，現有證據多是安眠藥停藥與依賴的安全性背景。
- 仿單警語與禁忌屬於阻斷性資料缺口，尚無法進入安全性篩選。
- 同一藥物的其他 9 個預測（如 ADHD、cauda equina syndrome 等）機轉連結薄弱，同樣列為 Hold。「失眠」與「sleep disorder, initiating and maintaining sleep」兩項證據高度重疊，不應視為獨立支持。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌、核准適應症），並確認失眠是否已在標示內。
- 補齊 DrugBank 的原適應症與作用機轉資料。
- 搜尋並評估 diazepam 對照安慰劑或其他安眠藥的失眠隨機對照試驗，尤其是短期使用的療效與次日功能影響。
- 擬定針對老年人與長期使用者的依賴、跌倒與認知風險監測與停藥計畫。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

