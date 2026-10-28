---
layout: default
title: Felodipine
parent: 僅模型預測 (L5)
nav_order: 366
evidence_level: L5
indication_count: 5
monitor_inn: "FELODIPINE"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-28
description: "Felodipine：預測新適應症為肺部疾病及/或缺氧所致肺高壓（證據等級 L5）。原適應症：高血壓"
---

# Felodipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Felodipine：從高血壓到肺部疾病及／或缺氧所致肺高壓
{: .text-alpha }

## 一句話總結

Felodipine 是二氫吡啶類鈣離子通道阻斷劑，知識圖譜中記錄的原適應症為高血壓。
TxGNN 模型預測它可能對**肺部疾病及/或缺氧所致肺高壓 (pulmonary hypertension owing to lung disease and/or hypoxia)** 有效，
但目前**沒有臨床試驗**，只有 **9 篇文獻**，且皆為非肺血管的前臨床缺氧模型，屬間接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓（知識圖譜記錄的關聯；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 肺部疾病及/或缺氧所致肺高壓 |
| TxGNN 預測分數 | 0.9991 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 16 張／共 16 張） |
| 許可證數 | 16 張（有效 16 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Felodipine 屬於二氫吡啶類 L 型鈣離子通道阻斷劑，一般認為會使血管平滑肌鬆弛、降低血管阻力。從機轉推想，鈣離子通道參與的肺血管收縮（包括缺氧性肺血管收縮）可能是一個潛在標的。

高血壓與肺高壓都涉及血管張力異常，這是模型預測的可能依據。不過，目前取得的文獻都是前臨床或非肺部缺氧模型（大鼠腎小管、人類心房肌、腦動脈、腦血流、行為學實驗等），顯示的是缺氧再灌流下的細胞保護與血管舒張作用，並未研究肺血管或肺高壓病人，因此連結只是間接的機轉推論。

另有一項重要的安全疑慮：鈣離子通道阻斷劑可能抑制缺氧性肺血管收縮，造成通氣灌流不匹配而使氣體交換惡化，因此一般不建議用於肺部疾病所致的肺高壓。這點必須先釐清，才能進一步考慮。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下列文獻均未直接研究肺高壓，皆為缺氧或缺血的前臨床模型。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8584414](https://pubmed.ncbi.nlm.nih.gov/8584414/) | 1995 | 前臨床（大鼠近端腎小管） | Pflugers Arch | Felodipine 可透過非鈣依賴機制保護腎小管免於缺氧損傷 |
| [9431863](https://pubmed.ncbi.nlm.nih.gov/9431863/) | 1997 | 前臨床（人類心房肌離體） | Int J Cardiol | Felodipine 預處理可保護心房肌免於缺氧再灌流功能障礙 |
| [8394565](https://pubmed.ncbi.nlm.nih.gov/8394565/) | 1993 | 前臨床（兔腎小管細胞） | Pflugers Arch | 探討 L 型鈣通道阻斷劑對缺氧引起細胞內鈣上升的影響 |
| [3961832](https://pubmed.ncbi.nlm.nih.gov/3961832/) | 1986 | 前臨床（大鼠腦血流） | Stroke | 二氫吡啶類可減弱缺氧引起的腦血流增加 |
| [3343292](https://pubmed.ncbi.nlm.nih.gov/3343292/) | 1988 | 前臨床（大鼠大腦皮質） | J Cereb Blood Flow Metab | Felodipine 抑制缺氧誘發的腺苷與肌苷釋放 |
| [8160846](https://pubmed.ncbi.nlm.nih.gov/8160846/) | 1994 | 前臨床（血管組織） | Am J Physiol | 先前的缺氧會減弱後續缺氧引起的血管舒張 |
| [3142891](https://pubmed.ncbi.nlm.nih.gov/3142891/) | 1988 | 前臨床（腦動脈） | J Cereb Blood Flow Metab | 研究血管擴張劑對再氧合與鈣誘發腦動脈收縮的影響 |
| [8110031](https://pubmed.ncbi.nlm.nih.gov/8110031/) | 1993 | 前臨床（動物行為） | Arch Int Pharmacodyn Ther | 比較三種鈣通道阻斷劑對缺氧大鼠被動迴避行為的影響 |
| [9864178](https://pubmed.ncbi.nlm.nih.gov/9864178/) | 1999 | 前臨床（體外嗜中性球） | Blood | 一氧化氮影響缺氧再氧合後嗜中性球自由基生成 |

## 香港上市資訊

香港共有 16 張單方許可證，皆為有效狀態（資料中未載明劑型與核准適應症文字）。以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-37191 | PLENDIL TAB 2.5MG EXTENDED RELEASE | 緩釋錠 | 資料未載明 |
| HK-32696 | PLENDIL TAB 5MG EXTENDED RELEASE | 緩釋錠 | 資料未載明 |
| HK-32695 | PLENDIL TAB 10MG EXTENDED RELEASE | 緩釋錠 | 資料未載明 |
| HK-38314 | LOGIMAX TAB EXTENDED RELEASE | 緩釋錠 | 資料未載明 |
| HK-49353 | FELODIPIN STADA RETARD TAB 5MG | 緩釋錠 | 資料未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：腎臟疾病、肝臟疾病、膽囊疾病、血管水腫、嗜中性白血球低下、無顆粒球症、主動脈瓣狹窄、低血壓、肥厚性心肌病變、心肌梗塞、冠狀動脈疾病、動脈粥樣硬化等。
- **藥物交互作用**：共查得 100 筆，主要例如：
  - 重大（Major）：Dolasetron
  - 中度（Moderate）：Clarithromycin、Cimetidine、Aprepitant、Bupropion，以及多種皮質類固醇（Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone）
- **預測適應症相關的疑慮**：鈣離子通道阻斷劑可能抑制缺氧性肺血管收縮而使氣體交換惡化。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 對於缺氧或肺部疾病所致肺高壓，沒有任何臨床試驗，也沒有直接研究該疾病的文獻，僅有模型預測與間接的前臨床資料，證據等級為 L5。
- 鈣離子通道阻斷劑可能使肺部疾病病人的氣體交換惡化，安全疑慮尚未釐清。

**其他預測適應症的簡述：**
- 多因素機轉不明的肺高壓、惡性高血壓腎病變、Braddock 症候群：僅有模型預測，無試驗與文獻，建議 Hold。
- 慢性肺心病：有 3 篇 1980 年代的小型血行動力學研究或回顧（含 COPD 病人的 felodipine 輸注研究），僅屬間接證據，沒有存活率或功能性結果，仍列為研究問題。

**若要推進需要：**
- 補齊作用機轉資料與香港仿單的警語、禁忌及核准適應症文字
- 針對肺血管與肺高壓病人的直接研究（含氣體交換與通氣灌流影響的評估）
- 確認是否存在對血管反應性試驗呈陽性、可能受益的特定族群
- 評估與常用藥物（如 CYP3A4 抑制劑）交互作用的風險管理計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

