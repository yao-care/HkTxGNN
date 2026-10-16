---
layout: default
title: Zanamivir
parent: 僅模型預測 (L5)
nav_order: 948
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Zanamivir：預測新適應症為腎盂腎炎 (Pyelonephritis)（證據等級 L5）。原適應症：流行性感冒 (Influenza)"
monitor_inn: "ZANAMIVIR"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
---

# Zanamivir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Zanamivir：從流行性感冒到腎盂腎炎

## 一句話總結

Zanamivir 是一種神經胺酸酶抑制劑，原本用於治療流行性感冒。
TxGNN 模型預測它可能對**腎盂腎炎 (Pyelonephritis)** 有效，但目前**沒有任何臨床試驗與相關文獻**支持這個方向，僅有模型預測分數。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 流行性感冒 (Influenza) |
| 預測新適應症 | 腎盂腎炎 (Pyelonephritis) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Zanamivir 是病毒神經胺酸酶抑制劑，其在流感中的療效已被證實。

然而，腎盂腎炎主要由細菌（如大腸桿菌）引起，Zanamivir 並不針對這些病原體。此外，吸入型 Zanamivir 的全身暴露量低，難以在腎臟或泌尿道達到有效濃度。部分細菌雖表現類似神經胺酸酶的唾液酸酶，但沒有證據顯示這與腎盂腎炎的治療效果有關。

因此，這項預測較可能是知識圖譜中與「感染」相關的關聯所造成的假象，而不是以機轉為基礎的訊號。

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
| HK-45843 | RELENZA POWDER FOR ORAL INHALATION 5MG | 吸入粉劑（依品名） | 資料未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物－疾病關聯資料，非仿單原文）：癲癇、慢性阻塞性肺病 (COPD)、支氣管疾病、譫妄。這些需由仿單進一步確認。
- **藥物交互作用**：共查得 8 筆。
  - 中度：人類胰島素（吸入型，速效）
  - 嚴重度未分級：Clarithromycin、Loratadine、Montelukast、Ketotifen、Fexofenadine、Ibuprofen、Diclofenac

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據僅有模型預測分數（L5），沒有臨床試驗或文獻支持。
- 機轉上不合理：Zanamivir 不作用於細菌性病原體，且吸入後全身暴露量低。

**若要推進需要：**
- 取得 Zanamivir 的作用機轉資料，並釐清是否對泌尿道病原體有任何活性
- 取得香港仿單的警語與禁忌症
- 取得任何支持腎盂腎炎的臨床前或臨床證據；若無，不建議進一步投入

---

*補充：TxGNN 排名第二的預測「酪胺酸代謝異常 (Disorder of Tyrosine Metabolism)」分數為 99.02%，但檢索到的 3 篇文獻都是流感神經胺酸酶抑制劑的抗藥性或檢測方法研究，與酪胺酸代謝疾病無關，應是關鍵字（tyrosine）造成的假關聯，同樣屬 L5、建議 Hold。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

