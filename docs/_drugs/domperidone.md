---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 1
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Domperidone：從消化道動力障礙到腎因性不適當抗利尿症候群

## 一句話總結

Domperidone 是一種多巴胺 D2/D3 受體拮抗劑，廣泛用於治療噁心、嘔吐及消化道動力障礙。
TxGNN 模型預測它可能對**腎因性不適當抗利尿症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效，
目前尚無任何臨床試驗或文獻直接支持此方向，屬於純模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 噁心、嘔吐、消化道動力障礙（依一般藥理知識；Evidence Pack 中無原適應症登錄） |
| 預測新適應症 | 腎因性不適當抗利尿症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| TxGNN 預測分數 | 99.08% |
| 證據等級 | L5 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（列為資料缺口 DG002）。根據已知藥理學資訊，Domperidone 是多巴胺 D2/D3 受體拮抗劑，主要作用於消化道及腦部化學感受觸發區（Chemoreceptor Trigger Zone, CTZ），用以促進胃腸蠕動並抑制嘔吐。

腎因性不適當抗利尿症候群（NSIAD）是由 *AVPR2*（精胺酸加壓素 V2 受體）的功能增益性突變（gain-of-function mutation）所引起的罕見 X 染色體連鎖遺傳疾病，導致腎小管對水分的非滲透壓依賴性過度再吸收，臨床表現為持續性低血鈉症。多巴胺訊號系統在腎臟近端小管及下視丘-垂體軸均具有調節功能，包括影響抗利尿激素（ADH/AVP）的釋放與腎臟水分處理。

從機轉推論的角度，多巴胺 D2 受體拮抗可能透過干預下視丘-垂體層級的 AVP 釋放調控，或透過腎臟多巴胺受體對腎小管功能的間接影響，與 NSIAD 的病生理路徑產生交叉。然而，此連結目前純屬機轉假說，**尚無任何直接研究加以驗證**，亦無相關臨床試驗或文獻可供佐證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

Domperidone 目前在台灣**未上市**，無藥品許可證登記資料，無法取得本地核准適應症或仿單資訊。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 注意：安全性警語、禁忌症及藥物交互作用資料均為資料缺口（DG001），目前無法進行安全性初評。若需推進，此為阻斷性（Blocking）缺口，須優先補充。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖達 99.08%，但目前完全缺乏任何臨床試驗或文獻支持 Domperidone 用於 NSIAD；加以該藥物在台灣未上市、安全性資料付之闕如，整體風險-效益評估不足以支持進入下一階段。

**若要推進需要：**
- 補充作用機轉資料（MOA），確認多巴胺 D2 拮抗是否與 AVPR2/AVP 信號通路存在可利用的交叉機制
- 進行前臨床研究（in vitro / in vivo），驗證 Domperidone 對 NSIAD 相關動物或細胞模型是否具有效果
- 從 TFDA 官網下載仿單 PDF，解析警語與禁忌症，補齊阻斷性安全性資料缺口（DG001）
- 評估台灣市場准入可行性（藥品目前未上市，需釐清引進路徑）
- 確認 NSIAD 作為孤兒藥適應症的市場規模與法規誘因（如罕見疾病認定資格）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

