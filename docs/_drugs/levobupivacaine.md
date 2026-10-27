---
layout: default
title: Levobupivacaine
parent: 僅模型預測 (L5)
nav_order: 523
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Levobupivacaine：預測新適應症為胃十二指腸炎 (Gastroduodenitis)（證據等級 L5）。原適應症：資料未記載"
monitor_inn: "LEVOBUPIVACAINE"
predicted_indications: ["gastroduodenitis"]
---

# Levobupivacaine
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

## Levobupivacaine：從局部麻醉到胃十二指腸炎
{: .text-alpha }

## 一句話總結

Levobupivacaine 是長效醯胺類局部麻醉藥，目前在香港已核准上市，但本次整理的資料中沒有記載核准適應症。
TxGNN 模型預測它可能對**胃十二指腸炎 (Gastroduodenitis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未記載（香港許可證未列適應症文字） |
| 預測新適應症 | 胃十二指腸炎 (Gastroduodenitis) |
| TxGNN 預測分數 | 99.09% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Levobupivacaine 是長效醯胺類局部麻醉藥，一般認為其作用是阻斷電壓門控鈉通道，但本次資料中未收錄正式的 MOA，也沒有可確認的原適應症。

一個可能但尚未驗證的推論是：鈉通道阻斷或許能降低上消化道黏膜的內臟痛覺訊號傳遞，或神經源性發炎。不過，沒有任何證據顯示它在胃十二指腸炎中有用，無論是全身或局部給藥。

需要注意的是，此預測分數雖高，但可能только反映知識圖譜的結構特性（例如與其他麻醉藥或消化道藥物共享相近節點），而非真正的治療效果。給藥途徑相容性也尚未評估。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67067 | LEVOBUPIVACAINE KABI SOLUTION FOR INJECTION/INFUSION 50MG/10ML（Fresenius Kabi） | 注射/輸注溶液 | 資料未記載 |
| HK-67344 | LEVOBUPIVACAINE SOLUTION FOR INJECTION OR INFUSION 50MG/10ML（Hong Kong Medical Supplies） | 注射/輸注溶液 | 資料未記載 |
| HK-67066 | LEVOBUPIVACAINE KABI SOLUTION FOR INJECTION/INFUSION 25MG/10ML（Fresenius Kabi） | 注射/輸注溶液 | 資料未記載 |

---

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病關聯，並非仿單內容）：腎臟疾病、輸尿管積膿、肝臟疾病、膽囊疾病、重症肌無力（含成人型）、神經肌肉接合部疾病、丁醯膽鹼酯酶缺乏症、心血管疾病、心臟疾病。
- **藥物交互作用**：共記錄 62 筆。主要的中度交互作用包括 Aprepitant、Cimetidine、Clarithromycin、Obeticholic acid、Miconazole、Clotrimazole、Cobicistat、Deferasirox、Ticlopidine、Fostamatinib、Thiabendazole、Primaquine，以及其他局部麻醉藥（Lidocaine、Benzocaine、Cocaine）。輕度者如 Dexamethasone、Omeprazole、Hyaluronidase、Albendazole。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數支持，沒有任何臨床試驗或文獻，證據等級為 L5。
- 原適應症與作用機轉資料都缺漏，無法建立機轉上的合理連結，而且知識圖譜顯示多項潛在禁忌疾病，交互作用也多。

**若要推進需要：**
- 取得香港仿單（核准適應症、警語、禁忌症）
- 補齊 DrugBank 的作用機轉資料
- 檢索局部麻醉藥或鈉通道阻斷劑用於胃十二指腸炎或上消化道疼痛的文獻與試驗
- 評估給藥途徑是否與目標適應症相容（目前許可證均為注射/輸注劑型）
- 進行前臨床或機轉研究，排除預測僅為知識圖譜假象的可能
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

