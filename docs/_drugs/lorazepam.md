---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 530
evidence_level: L5
indication_count: 5
---

# Lorazepam
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

# Lorazepam：從苯二氮平類鎮靜藥物到三叉神經腫瘤（預測）

## 一句話總結

Lorazepam 是一種苯二氮平類（benzodiazepine）藥物，作用於 GABA-A 受體。
TxGNN 模型預測它可能對**三叉神經腫瘤 (Trigeminal Nerve Neoplasm)** 有效。
目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未提供適應症文字 |
| 預測新適應症 | 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Lorazepam 是 GABA-A 受體的正向異位調節劑（positive allosteric modulator），能增強 GABA 介導的神經抑制，產生鎮靜、抗焦慮、抗痙攣等作用。DrugBank 的作用機轉欄位目前缺漏，以上為藥物類別層級的已知資訊。

從機轉看，這個預測**缺乏合理性**。GABA-A 增強作用與抗腫瘤活性沒有明確關聯，也沒有任何資料顯示 lorazepam 能抑制腫瘤生長。三叉神經屬於神經系統，模型分數偏高，較可能是知識圖譜中「神經系統關聯」造成的假象，而非真正的老藥新用訊號。

99.87% 的分數只代表模型內部的關聯強度，不等於臨床有效機率。在沒有任何實證支持下，不宜當作再利用依據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 9 張 lorazepam 許可證，以下列出 5 張主要許可證（資料未提供劑型與核准適應症）：

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-63368 | PMS-LORAZEPAM TABLETS 0.5MG | TRENTON-BOMA LTD |
| HK-63367 | PMS-LORAZEPAM TABLETS 1MG | TRENTON-BOMA LTD |
| HK-63369 | PMS-LORAZEPAM TABLETS 2MG | TRENTON-BOMA LTD |
| HK-34394 | SILENCE TAB 1MG | YUNG SHIN CO LTD |
| HK-35048 | LORANS 2 TAB 2MG | STAR MEDICAL SUPPLIES LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有任何臨床試驗或文獻（L5），且 lorazepam 的 GABA-A 機轉與抗腫瘤作用之間沒有合理連結，很可能是神經系統關聯造成的假象。
- 即使暫停這個適應症，lorazepam 在其他預測適應症上（例如失眠、反射性癲癇）已有部分文獻，可另案評估。

**若要推進需要：**
- 建立從 GABA-A 調節到三叉神經腫瘤的機轉假說，並以細胞或動物模型驗證。
- 補齊 DrugBank 的原適應症與作用機轉資料。
- 取得香港衛生署仿單，確認警語與禁忌。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

