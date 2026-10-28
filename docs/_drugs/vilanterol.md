---
layout: default
title: Vilanterol
parent: 僅模型預測 (L5)
nav_order: 934
evidence_level: L5
indication_count: 6
monitor_inn: "VILANTEROL"
predicted_indications: ["hyperlucent lung", "tracheal stenosis", "bronchial neoplasm (disease)", "respiratory malformation", "tracheal calcification", "laryngotracheitis"]
last_modified_at: 2026-10-23
description: "Vilanterol：預測新適應症為過度透亮肺 (hyperlucent lung)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Vilanterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Vilanterol: 過度透亮肺 (hyperlucent lung)
{: .text-alpha }

> 說明：本報告以預測排名第 1 的「過度透亮肺 (Hyperlucent lung)」為主要預測新適應症；排名第 3 的支氣管腫瘤是唯一有直接相關試驗與文獻的項目，於下文一併說明。

---

## 一句話總結

Vilanterol 是一種吸入型長效 β2 受體促效劑，知識圖譜中記錄的原適應症為慢性阻塞性肺病 (COPD)、氣喘、支氣管炎與肺氣腫。
TxGNN 模型預測它可能對**過度透亮肺 (Hyperlucent lung)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持，屬於僅有模型預測的階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 過度透亮肺 (hyperlucent lung) |
| TxGNN 預測分數 | 0.9972 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Vilanterol 屬於吸入型長效 β2 受體促效劑，一般認為其作用是透過放鬆支氣管平滑肌來緩解氣道阻塞。

過度透亮肺（例如 Swyer-James 症候群、類肺氣腫的過度充氣）以氣流阻塞與空氣滯留為特徵，與知識圖譜中記錄的 COPD、肺氣腫關係相近，因此模型給出高分。機轉上，支氣管擴張可能緩解其中可逆的氣流受限成分。

不過，這僅是模型預測，沒有試驗或文獻佐證，且與既有的 COPD／肺氣腫關係高度重疊，並不代表是真正的新用途。

---

## 臨床試驗證據

預測新適應症「過度透亮肺」目前無相關臨床試驗登記。

作為參考，排名第 3 的「支氣管腫瘤」有下列試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04536675](https://clinicaltrials.gov/study/NCT04536675) | Phase 3 | 進行中（已停止招募） | 204 | 評估圍手術期固定劑量雙重支氣管擴張劑對接受肺癌手術的輕中度 COPD 病人術後肺功能的影響；尚無結果，終點為肺功能而非腫瘤療效 |

---

## 文獻證據

預測新適應症「過度透亮肺」目前無相關文獻。

作為參考，排名第 3 的「支氣管腫瘤」有下列文獻（皆屬 COPD 合併肺癌的情境，並非針對腫瘤本身的療效）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39607005](https://pubmed.ncbi.nlm.nih.gov/39607005/) | 2024 | 臨床研究 | Future Oncology | 分析雙重支氣管擴張劑搭配術前復健，用於可手術的非小細胞肺癌合併 COPD 病人 |
| [33422241](https://pubmed.ncbi.nlm.nih.gov/33422241/) | 2021 | 病例報告 | Chest | 一位 COPD 病人反覆急性惡化並有支氣管內病灶的病例 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62693 | RELVAR ELLIPTA 吸入粉劑 100mcg/25mcg | 吸入粉劑 | 許可證資料未載明 |
| HK-62694 | RELVAR ELLIPTA 吸入粉劑 200mcg/25mcg | 吸入粉劑 | 許可證資料未載明 |
| HK-63414 | ANORO ELLIPTA 吸入粉劑 62.5mcg/25mcg | 吸入粉劑 | 許可證資料未載明 |
| HK-65911 | TRELEGY ELLIPTA 吸入粉劑 100mcg/62.5mcg/25mcg | 吸入粉劑 | 許可證資料未載明 |
| HK-67942 | TRELEGY ELLIPTA 吸入粉劑 200mcg/62.5mcg/25mcg | 吸入粉劑 | 許可證資料未載明 |

---

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為部分例子：
  - 中度：糖尿病用藥（Acarbose、Alogliptin、Canagliflozin、Dapagliflozin、Empagliflozin、Dulaglutide）、Clarithromycin、Cisapride、Dolasetron、Ephedrine、Epinephrine
  - 輕度：皮質類固醇（Beclomethasone、Betamethasone、Budesonide、Dexamethasone）

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 過度透亮肺僅有模型預測，無任何臨床試驗或文獻直接研究，證據等級為 L5。
- 此預測與既有的 COPD／肺氣腫關係重疊，並非明確的新用途；其餘高分預測（氣管狹窄、氣管鈣化、喉氣管炎）機轉上也較薄弱。

**若要推進需要：**
- 取得 Vilanterol 的作用機轉資料與香港仿單中的核准適應症、警語及禁忌症
- 以臨床專家確認過度透亮肺中是否存在可逆的氣流阻塞成分
- 搜尋並建立直接針對該疾病的病例系列或臨床研究
- 若關注支氣管腫瘤方向，需待 NCT04536675 結果，且應視為併存 COPD 的支持性照護，而非抗腫瘤治療
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

