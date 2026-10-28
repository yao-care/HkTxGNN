---
layout: default
title: Flunitrazepam
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 8
monitor_inn: "FLUNITRAZEPAM"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "anxiety", "anxiety disorder", "alcohol withdrawal delirium", "agoraphobia", "benign paroxysmal torticollis of infancy", "atrophoderma vermiculata"]
last_modified_at: 2026-10-23
description: "Flunitrazepam：預測新適應症為偏頭痛（證據等級 L5）。原適應症：香港許可證資料未載明"
---

# Flunitrazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Flunitrazepam：偏頭痛的藥物再利用評估
{: .text-alpha }

## 一句話總結

Flunitrazepam（氟硝西泮）是苯二氮平類藥物，主要作用於 GABA-A 受體，藥理資料庫列出的臨床用途為嚴重失眠。
TxGNN 模型預測它可能對**偏頭痛**有效，但目前**沒有任何臨床試驗或文獻**直接研究這個方向，證據僅來自模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明（藥理資料庫列為嚴重失眠，非許可證文字） |
| 預測新適應症 | 偏頭痛 |
| TxGNN 預測分數 | 0.9971 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Flunitrazepam 是 GABA-A 受體的正向異位調節劑，藥理資料顯示它與 GABA-A 受體 α1、α2、α3、α5 亞單位結合。

理論上，增強 GABA 抑制性傳導可能影響大腦皮質的過度興奮，這是偏頭痛的病理機轉之一，因此模型給出高分。但這只是推測：苯二氮平類並非公認的偏頭痛治療藥物，且有依賴與濫用風險。

此外，TxGNN 模型（深度學習）也給出了偏頭痛相關疾病（如伴腦幹先兆的偏頭痛、嬰兒良性陣發性斜頸）高分。這些分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-56628 | FLUNITA TAB 1MG | JEAN-MARIE PHARMACAL CO LTD |
| HK-34683 | FLUNITA TAB 2MG | JEAN-MARIE PHARMACAL CO LTD |
| HK-12370 | ROHYPNOL TAB 1MG | DKSH HONG KONG LIMITED |

三張許可證在本報告彙整的資料中，劑型與核准適應症欄位皆為空白，請以原廠仿單為準。

---

## 安全性考量

- **藥理作用靶點**：與 GABA-A 受體 α1、α2、α3、α5 亞單位結合。這是靶點資料，不是藥物交互作用清單。
- **文獻中反覆出現的風險（來自其他適應症的檢索結果）**：
  - 濫用與依賴風險，並有被用作迷姦藥物的報告。
  - 劑量相關的記憶與精神動作功能受損、順行性失憶。
  - 與酒精併用有加成效應。
  - 可能出現躁動、攻擊等矛盾反應。

其餘警語、禁忌症與藥物交互作用，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 偏頭痛沒有任何臨床試驗或文獻支持，只有模型分數，屬於 L5。
- 苯二氮平類在偏頭痛中缺乏地位，而 Flunitrazepam 的濫用與依賴風險明顯，效益風險比不佳。

**若要推進需要：**
- 系統性檢索 GABA-A 調節劑用於偏頭痛的臨床與前臨床研究，確認是否存在直接證據。
- 取得完整的作用機轉資料，並釐清偏頭痛病理與 GABA 傳導的關聯。
- 取得香港仿單中的警語、禁忌症與原核准適應症。
- 與已有成熟證據的偏頭痛治療相比，評估是否有任何差異化價值。

**補充觀察：** 同批預測中，「酒精戒斷譫妄」有靜脈注射 Flunitrazepam 的臨床報告（如 PMID 8214408），但多為早期開放性或初步研究，且已有地西泮、勞拉西泮等替代藥物。若要優先評估其他方向，可從此處著手，但那是另一份獨立評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

