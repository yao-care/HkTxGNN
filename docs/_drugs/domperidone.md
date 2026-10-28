---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Domperidone：預測新適應症為腎因性抗利尿不適當症候群 (NSIAD)（證據等級 L5）。原適應症：香港許可證未載明核准適應症文字"
monitor_inn: "DOMPERIDONE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Domperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Domperidone：從消化道症狀（適應症資料缺失）到腎因性抗利尿不適當症候群
{: .text-alpha }

## 一句話總結

Domperidone 是週邊多巴胺 D2/D3 受體拮抗劑，臨床上用於處理消化不良、胃灼熱、上腹痛、噁心與嘔吐。
TxGNN 模型預測它可能對**腎因性抗利尿不適當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症文字（藥理資料顯示用於消化不良、噁心、嘔吐等） |
| 預測新適應症 | 腎因性抗利尿不適當症候群 (NSIAD) |
| TxGNN 預測分數 | 0.9908 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 domperidone 是週邊多巴胺 D2/D3 受體拮抗劑（標靶為 DRD2、DRD3），作為促腸胃蠕動與止吐藥使用。

NSIAD 是由血管加壓素 V2 受體 (AVPR2) 的功能獲得性突變所致，會在沒有血管加壓素的情況下造成水分滯留與低血鈉。目前並無已知路徑將 D2 拮抗作用與 V2 受體活性或腎臟水分處理連結起來。

因此，這個預測分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性（例如低血鈉、水分平衡相關疾病），而非生物學證據。此連結目前仍屬推測，若要進一步考慮，需先有合理的標靶層級論證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 20 張有效單方許可證，以下列出 5 張代表性許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-58627 | APO-DOMPERIDONE TAB 10MG | HIND WING CO LTD |
| HK-64541 | DOSIN TABLETS 10MG | TOP HARVEST PHARMACEUTICALS COMPANY LIMITED |
| HK-48289 | NIDOLIUM TAB 10MG | SUNTOL MEDICAL LIMITED |
| HK-44630 | DOMPEON TAB 10MG | NEOCHEM PHARMACEUTICAL LABORATORIES LTD. |
| HK-50698 | VICKTILIN SYRUP 5MG/5ML | VICKMANS LABORATORIES LTD |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜的藥物－疾病禁忌關係，非仿單文字）：長 QT 症候群、家族性長 QT 症候群、尖端扭轉型心室頻脈 (torsades de pointes)、肝臟疾病、膽囊疾病。
- **QT 風險**：domperidone 具有 QT 延長與心律不整風險。NSIAD 患者常有低血鈉與電解質異常，而這些本身是 QT 相關事件的危險因子，此族群可能特別脆弱。
- **藥理交互作用紀錄**：共 2 筆，皆為藥理標靶紀錄（D2 受體、D3 受體），並非藥物間交互作用。

其餘警語與禁忌症資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數（0.9908），沒有臨床試驗或文獻佐證，且 D2/D3 拮抗與 V2 受體或腎臟水分處理之間缺乏已知機轉連結。
- 目標族群的低血鈉與電解質異常會加重 domperidone 的 QT 風險，安全性疑慮明顯。

**若要推進需要：**
- 提出標靶層級的合理機轉假說（D2/D3 或其他路徑如何影響 AVPR2 或腎臟水分處理）
- 取得完整作用機轉資料（MOA）
- 取得香港仿單的警語與禁忌症，完成安全性篩選
- 進行文獻與臨床前研究的系統性檢索，確認是否有任何支持證據
- 若未來考慮推進，需先評估 QT 與電解質監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

