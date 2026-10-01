---
layout: default
title: Sevoflurane
parent: 僅模型預測 (L5)
nav_order: 796
evidence_level: L5
indication_count: 5
---

# Sevoflurane
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

# Sevoflurane：從全身麻醉到變異型心絞痛（Prinzmetal angina）

## 一句話總結

Sevoflurane（七氟烷）是吸入式全身麻醉劑，在香港已有 3 張上市許可證。
TxGNN 模型預測它可能對**變異型心絞痛 (Prinzmetal angina)** 有效，但目前**沒有臨床試驗，也沒有相關文獻**，只有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明；依藥物類別為吸入式全身麻醉 |
| 預測新適應症 | 變異型心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Sevoflurane 屬於揮發性麻醉劑，這類藥物已知會使血管平滑肌放鬆，可能透過調節鈣離子通道而減少冠狀動脈痙攣。

變異型心絞痛的主要病生理是冠狀動脈痙攣，因此「放鬆血管平滑肌」在生物學上說得通。但這個關聯是推論，輸入資料沒有機轉文獻佐證。

Sevoflurane 是全身麻醉劑，需在麻醉環境下使用，不適合作為長期抗心絞痛藥物。即使機轉合理，實務上的可行性也很低。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-40147 | SEVORANE INHALATION LIQUID | ABBVIE LIMITED |
| HK-57565 | SEVOFLURANE INHALATION ANESTHETIC LIQUID (BAXTER) | BAXTER HEALTHCARE LIMITED |
| HK-56752 | SOJOURN LIQUID FOR INHALATION | HONG KONG MEDICAL SUPPLIES LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數支持，沒有任何試驗或文獻。
- 藥物本身是全身麻醉劑，不適合長期治療心絞痛。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認警語與禁忌症
- 補充 Sevoflurane 的作用機轉資料，例如查詢 DrugBank
- 搜尋 Sevoflurane 與冠狀動脈痙攣、心肌保護相關的機轉或臨床研究
- 評估是否有可行的給藥途徑，因為目前路徑相容性尚未評估

**其他候選適應症（供參考）：** 其餘 4 個預測也都是 Hold。
- 纖維肌痛症：只有 1 篇麻醉處置的病例報告，並非治療證據。
- 肌腱炎：檢索到的文獻都只是手術中使用麻醉的關鍵字比對，不能視為支持。
- 妥瑞氏症與纖維性肌炎：沒有任何證據。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

