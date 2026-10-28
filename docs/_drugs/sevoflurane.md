---
layout: default
title: Sevoflurane
parent: 僅模型預測 (L5)
nav_order: 811
evidence_level: L5
indication_count: 10
monitor_inn: "SEVOFLURANE"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "fibromyalgia", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "migraine disorder", "inclusion body myositis"]
last_modified_at: 2026-10-23
description: "Sevoflurane：預測新適應症為變異型心絞痛 (Prinzmetal angina)（證據等級 L5）。原適應症：本次整理的資料中，許可證未載明核准適應症文字"
---

# Sevoflurane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Sevoflurane：從全身麻醉到變異型心絞痛（Prinzmetal angina）
{: .text-alpha }

## 一句話總結

Sevoflurane 是一種吸入式全身麻醉劑，已在香港取得 3 張有效許可證。
TxGNN 模型預測它可能對**變異型心絞痛 (Prinzmetal angina)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次整理的資料中，許可證未載明核准適應症文字 |
| 預測新適應症 | 變異型心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 0.9978 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Sevoflurane 屬於揮發性吸入麻醉劑，一般認為作用於 GABA-A 與 NMDA 受體等中樞神經路徑。

從理論上看，揮發性麻醉劑可能經由鈣離子通道調節與血管平滑肌鬆弛影響冠狀動脈的血管收縮，這是此預測唯一可推測的機轉關聯。然而，Sevoflurane 在冠狀動脈痙攣上並無已證實的治療角色，這個關聯目前只是推測。

此預測分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據；沒有實際研究佐證，應視為提出假說的起點，而非治療建議。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-40147 | SEVORANE INHALATION LIQUID | 吸入液 | 資料未載明 |
| HK-57565 | SEVOFLURANE INHALATION ANESTHETIC LIQUID (BAXTER) | 吸入麻醉液 | 資料未載明 |
| HK-56752 | SOJOURN LIQUID FOR INHALATION | 吸入液 | 資料未載明 |

三張許可證均為單一成分製劑且狀態有效。

## 安全性考量

- **知識圖譜中記錄的禁忌關係**（來自知識圖譜，並非仿單文字）：癲癇、腎臟疾病、肝臟疾病、膽囊疾病、低血壓疾患、惡性高熱（麻醉相關及運動誘發）、假性腦瘤、顱內高壓、杜顯氏肌失養症及其他肌失養症、蛋白尿等。其中惡性高熱與肌肉疾病為揮發性麻醉劑的重要風險。
- **藥物交互作用**：資料庫共記錄 100 筆，列出的項目中屬重大等級者包括：
  - Epinephrine
  - Dolasetron
  - Cisapride

  其餘多為中度，例如 Morphine、Ondansetron、Clarithromycin、Levofloxacin 等。

正式警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何直接研究變異型心絞痛的臨床試驗或文獻，證據等級為 L5。
- Sevoflurane 是需在監測下使用的全身麻醉劑，用於需要長期處置的冠狀動脈痙攣並不實際，且已知對低血壓等族群有風險。

**若要推進需要：**
- 取得 Sevoflurane 的作用機轉資料，並分析其與冠狀動脈血管張力的關聯
- 進行前臨床或機轉研究，評估對冠狀動脈痙攣的影響
- 取得香港仿單的警語與禁忌，完成安全性初篩
- 評估給藥途徑與使用情境是否可行

---

### 附註：其他排名較前的預測

本次整理的其他預測適應症皆為 Hold。以下依 TxGNN 模型（深度學習）分數排序，分數可能反映模型從相關疾病之間學到的相似性，而非生物學證據，且均無直接研究該疾病治療效果的臨床試驗或文獻，因此證據等級皆為 L5。

| 排名 | 預測適應症 | TxGNN 分數 | 說明 |
|------|-----------|-----------|------|
| 2 | Tourette 症候群 | 0.9950 | 僅為模型預測 |
| 3 | 纖維肌痛症 | 0.9942 | 僅有 1 篇麻醉處置個案報告，屬圍手術期照護，並非疾病治療證據 |
| 4 | 肌腱炎 | 0.9941 | 文獻中 Sevoflurane 僅為肌腱相關手術的背景麻醉 |
| 5 | 纖維化肌炎 | 0.9941 | 僅為模型預測 |
| 6 | 特發性肉芽腫性肌炎 | 0.9941 | 僅為模型預測 |
| 7 | 腎因性抗利尿激素分泌不適當症候群 | 0.9940 | 僅為模型預測，且作用路徑無已知關聯 |
| 8 | 拔毛症 | 0.9933 | 僅為模型預測 |
| 9 | 偏頭痛 | 0.9923 | 唯一文獻為兒童 MRI 麻醉，並非偏頭痛治療研究 |
| 10 | 包涵體肌炎 | 0.9909 | 唯一文獻為麻醉考量個案報告，屬圍手術期安全性討論 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

