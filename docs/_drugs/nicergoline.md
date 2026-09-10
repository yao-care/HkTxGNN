---
layout: default
title: Nicergoline
parent: 僅模型預測 (L5)
nav_order: 522
evidence_level: L5
indication_count: 5
---

# Nicergoline
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

# Nicergoline：從腦血管疾病到多毛症（Hypertrichosis）

## 一句話總結

Nicergoline 是一種半合成麥角生物鹼衍生物，目前香港未上市，其正式適應症與作用機轉資料皆缺失。TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效，但目前**沒有任何臨床試驗**，**沒有任何文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無記錄（香港無許可證資料，原適應症未登載） |
| 預測新適應症 | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Nicergoline 的正式作用機轉資料目前缺失。根據評估包中其他候選適應症的推論描述，可知它是半合成麥角生物鹼衍生物，具有血管擴張、抗血小板及神經營養作用，藥理背景與 α1-腎上腺素受體拮抗活性有關——但這屬於背景推論，並非正式登載的 MOA。

多毛症與 Nicergoline 原本設定的血管相關用途之間，唯一提出的關聯是類比 minoxidil（同樣會誘發多毛症的副作用）。但這個類比機轉上站不住腳：minoxidil 誘發毛髮生長是透過開啟 K+ 通道，而 Nicergoline 的作用是 α1-腎上腺素受體拮抗，兩者機轉完全不同。

因此這個預測目前判斷為 TxGNN embedding 相似性造成的雜訊連結，缺乏機轉合理性與任何實證支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

本藥物尚未於香港取得許可證（0 張登記），無上市資料可供列示。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖高（99.57%），但無任何臨床試驗或文獻佐證，機轉類比（minoxidil）證據薄弱且作用途徑不同；加上此藥物在香港未上市、原適應症與安全性資料皆缺失，目前不具備推進條件。

**若要推進需要：**
- 補齊 TFDA／原廠仿單警語與禁忌症資料（現列為 Blocking 缺口）
- 補齊正式作用機轉 (MOA) 資料
- 以體外或動物實驗驗證 α1-拮抗活性是否確實影響毛囊/皮膚微循環
- 若證據仍無法補強，建議改聚焦本評估包中證據等級較高的候選（如良性攝護腺肥大，已有明確 α1-blocker class-effect 機轉可作研究假說）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

