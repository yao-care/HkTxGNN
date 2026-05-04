---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
---

# Entacapone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Entacapone：從帕金森氏症到 PLA2G6 相關神經退化症

## 一句話總結

Entacapone 是兒茶酚-O-甲基轉移酶（COMT）抑制劑，原本作為左旋多巴的輔助療法，用於帕金森氏症的運動波動控制。
TxGNN 模型預測它可能對 **PLA2G6 相關神經退化症（PLA2G6-associated neurodegeneration）** 有效，
然而目前尚無臨床試驗或文獻直接支持這個方向，建議暫緩推進並補充前臨床機轉資料。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 帕金森氏症（左旋多巴輔助療法，控制劑末運動波動） |
| 預測新適應症 | PLA2G6 相關神經退化症（PLA2G6-associated neurodegeneration） |
| TxGNN 預測分數 | 99.76% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Entacapone 的詳細作用機轉資料。根據已知資訊，Entacapone 是選擇性、可逆性的 COMT 抑制劑，透過阻斷多巴胺的甲基化代謝途徑，延長左旋多巴在腦內的作用時間，從而改善帕金森氏症患者的運動功能波動。

PLA2G6 相關神經退化症（PLAN）是由 *PLA2G6* 基因突變引起的罕見神經退化性疾病，表現型涵蓋嬰兒神經軸突性肌張力不全（INAD）、非典型神經軸突性肌張力不全，以及 **PLA2G6 相關肌張力不全-帕金森氏症候群**。最後一種亞型在病理機轉上與帕金森氏症高度重疊，涉及多巴胺能神經元退化、黑質萎縮及鐵沉積，為 TxGNN 模型預測的潛在機轉基礎——COMT 抑制若能提高殘存多巴胺能神經元的傳遞效率，理論上可能改善帕金森氏症樣症狀。

然而，Entacapone 在 PLAN 的藥理連結目前仍屬推論性質。*PLA2G6* 基因主要編碼鈣非依賴性磷脂酶 A2，其缺失導致膜磷脂代謝異常與軸突腫脹，與 COMT 抑制機轉並無直接的上下游關係。目前缺乏任何前臨床或臨床試驗資料支持此再利用假說，需謹慎評估可行性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Entacapone 目前在香港尚未取得上市許可（未上市，許可證數：0 張）。如需取得藥物，需透過特殊輸入申請或同情使用途徑。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖高（99.76%），但目前對於 PLA2G6 相關神經退化症，Entacapone 的再利用僅有模型預測支持，完全缺乏前臨床與臨床研究資料（L5 等級）。加之 Entacapone 在香港尚未上市，監管路徑未明，現階段不建議直接推進。

**若要推進需要：**

- **補充作用機轉資料**：查詢 DrugBank API 取得 Entacapone 完整 MOA，評估與 PLAN 病理機轉的真實連結強度
- **前臨床機轉研究**：探索 COMT 抑制是否能在 *PLA2G6* 基因敲除動物模型或 iPSC 衍生神經元中改善多巴胺傳遞
- **亞型聚焦**：優先評估 PLA2G6 相關肌張力不全-帕金森氏症候群（與帕金森氏症機轉最相近的亞型）
- **補充安全性資料**：取得 TFDA/EMA 仿單，確認警語、禁忌症及主要藥物交互作用
- **香港監管評估**：確認同情使用或臨床試驗申請可行性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

