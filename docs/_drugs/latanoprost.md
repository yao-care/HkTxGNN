---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 513
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Latanoprost：預測新適應症為原發性遺傳性青光眼 (Primary Hereditary Glaucoma)（證據等級 L5）。原適應症：開放性青光眼、高眼壓症"
monitor_inn: "LATANOPROST"
predicted_indications: ["visceral calciphylaxis", "hypotrichosis simplex of the scalp", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome"]
---

# Latanoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Latanoprost：從開放性青光眼到原發性遺傳性青光眼
{: .text-alpha }

## 一句話總結

Latanoprost 是前列腺素 F2α 類似物，原本用於開放性青光眼與高眼壓症的治療。
TxGNN 模型預測它可能對**原發性遺傳性青光眼 (Primary Hereditary Glaucoma)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 開放性青光眼、高眼壓症 |
| 預測新適應症 | 原發性遺傳性青光眼 (Primary Hereditary Glaucoma) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（列為研究問題，待補充證據） |

---

## 為什麼這個預測合理？

Latanoprost 是前列腺素 F2α 類似物，主要透過增加葡萄膜鞏膜途徑（以及較小程度的小樑網途徑）的房水流出來降低眼內壓。本報告所整理的資料中缺乏詳細的作用機轉記錄，以上機轉說明來自藥理學的一般知識。

原發性遺傳性青光眼（例如與 CYP1B1 變異相關的原發性先天性青光眼）同樣以眼壓升高為主要可介入的因素，因此降眼壓藥物在機轉上有相關性。

不過需要留意：這類遺傳性青光眼常涉及小樑網與前房角的發育異常，藥物治療通常只是手術前的暫時性橋接。0.999 的高分很可能反映了它在知識圖譜中與已核准青光眼適應症的距離相近，而非獨立的證據。兒童族群的專屬資料也需另行取得。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 20 張有效許可證（皆為單方登記，無已註銷者），以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-42158 | XALATAN EYE DROPS 50UG/ML（Viatris） | 眼藥水 | 資料未提供 |
| HK-64160 | XALAPRO EYE DROPS 0.005% W/V（Aspen） | 眼藥水 | 資料未提供 |
| HK-61876 | LATANOPROST OPHTHALMIC SOLUTION 0.005% W/V（Bausch & Lomb） | 眼藥水 | 資料未提供 |
| HK-65985 | MONOPOST EYE DROPS 50MCG/ML | 眼藥水 | 資料未提供 |
| HK-68150 | ROCKLATAN EYE DROPS（Santen） | 眼藥水 | 資料未提供 |

另有含 timolol 的複方產品（如 XALACOM、LATANOPROST AND TIMOLOL STADA 等），在資料中亦登記為有效許可證。

---

## 安全性考量

- **知識圖譜標示的相關疾病（非仿單內容）**：葡萄膜炎、虹膜疾病、睫狀體疾病、全葡萄膜炎、黃斑部視網膜水腫、囊樣黃斑水腫、虹膜炎、結膜炎（含急性傳染性結膜炎）。使用於這些眼部發炎或黃斑水腫相關情況時需特別謹慎。
- **藥物交互作用**：資料庫查詢到 100 筆交互作用紀錄，但嚴重程度皆標示為「未知」，例如 calcitriol、glimepiride、doxycycline、atropine、prednisone、triamcinolone 等，臨床意義尚待確認。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測，沒有臨床試驗或文獻佐證（L5）。高分可能來自與原適應症的圖譜鄰近性。
- 遺傳性青光眼多涉及結構性發育異常，藥物僅為輔助或暫時性處置，且兒童族群資料缺乏。

**若要推進需要：**
- 系統性檢索原發性先天性／遺傳性青光眼使用 latanoprost 的臨床與文獻證據
- 兒童族群的療效與安全性資料
- 取得香港仿單的警語、禁忌症與核准適應症
- 補充詳細的作用機轉資料
- 釐清 DDI 的實際嚴重程度分級

---

### 其他預測適應症的補充說明

| 預測適應症 | TxGNN 分數 | 評估 |
|-----------|-----------|------|
| 內臟鈣化防禦 (Visceral calciphylaxis) | 99.83% | Hold：無明確機轉依據，眼用劑量的全身暴露極低 |
| 頭皮單純性毛髮稀少 (Hypotrichosis simplex of the scalp) | 99.81% | 研究問題：前列腺素類似物可延長生長期（睫毛增生為已知副作用），機轉合理，但遺傳缺陷是否可被克服、頭皮給藥劑型皆未建立 |
| 動脈型胸廓出口症候群 | 99.78% | Hold：屬機械性壓迫，無支持證據 |
| 靜脈型胸廓出口症候群 | 99.78% | Hold：無可信的機轉角色 |

以上四項皆無臨床試驗或文獻支持，均為 L5 證據等級。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

