---
layout: default
title: Chlorobutanol
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Chlorobutanol：預測新適應症為勃起功能障礙 (Erectile Dysfunction)（證據等級 L5）。原適應症：香港許可證未載明核准適應症（產品品名顯示為牙痛滴劑與乳膏類）"
monitor_inn: "Chlorobutanol"
predicted_indications: ["erectile dysfunction (disease)", "migraine disorder", "migraine with brainstem aura", "Tourette syndrome", "trichotillomania", "attention deficit-hyperactivity disorder", "migraine with or without aura, susceptibility to", "localized pagetoid reticulosis", "faciodigitogenital syndrome", "atrophoderma vermiculata"]
---

# Chlorobutanol
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

# Chlorobutanol：從（原適應症未載明）到勃起功能障礙

## 一句話總結

Chlorobutanol 是氯醛衍生物，具鎮靜、安眠與局部麻醉特性，主要用作防腐劑，目前在香港有 3 張有效許可證，皆為單方製劑。
TxGNN 模型預測它可能對**勃起功能障礙 (Erectile Dysfunction)** 有效（分數 99.79%）。
但目前**沒有任何臨床試驗或文獻**支持這個預測，僅屬模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症（產品品名顯示為牙痛滴劑與乳膏類） |
| 預測新適應症 | 勃起功能障礙 (Erectile Dysfunction) |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Chlorobutanol 是氯醛衍生物，具鎮靜、安眠與局部麻醉作用，臨床上主要作為製劑的防腐劑。

現有資料中，沒有任何機轉路徑能把 Chlorobutanol 與勃起功能連結起來。0.998 的高分是知識圖譜的計算結果，不等於藥理上的合理性，也缺乏臨床或文獻佐證。因此目前不能認為這個預測有實質支持。

其他預測適應症同樣停留在模型層級，且都沒有試驗或文獻：

| 排名 | 預測適應症 | TxGNN 分數 | 備註 |
|------|-----------|-----------|------|
| 2 | 偏頭痛 (Migraine Disorder) | 99.71% | 鎮靜或中樞抑制作用理論上可能影響頭痛症狀，但屬推測 |
| 3 | 腦幹先兆偏頭痛 | 99.58% | 可能源自偏頭痛節點的相似性，無獨立證據 |
| 4 | 妥瑞氏症 (Tourette Syndrome) | 99.54% | 僅可想像非特異性中樞抑制作用，無支持 |
| 5 | 拔毛症 (Trichotillomania) | 99.50% | 可能反映神經精神疾病的圖譜鄰近關係 |
| 6 | 注意力不足過動症 (ADHD) | 99.41% | 鎮靜安眠類藥物無已知治療依據 |
| 7 | 偏頭痛易感性（基因） | 99.34% | 屬遺傳易感性實體，可能是圖譜傳播的假象 |
| 8 | 局部性類佩吉特網狀細胞增生症 | 99.20% | 罕見皮膚 T 細胞淋巴瘤變異型，無合理連結 |
| 9 | 面指趾生殖器症候群 | 99.19% | 罕見遺傳發育疾病，小分子藥物不太可能改變其生物學 |
| 10 | 蠕蟲狀萎縮性皮膚病 | 99.11% | 罕見皮膚萎縮性疾病，無支持 |

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
| HK-01662 | FACHEN TOOTHACHE DROPS | 未載明 | 未載明 |
| HK-47618 | FAZIG TOOTHACHE DROPS | 未載明 | 未載明 |
| HK-04644 | FUNGIFAX CREAM | 未載明 | 未載明 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症僅有 TxGNN 模型分數，沒有臨床試驗、文獻或明確機轉支持，證據等級為 L5。
- 作用機轉與香港仿單的警語及禁忌資料都缺失，目前無法進行安全性篩選。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，確認是否存在連結勃起功能或偏頭痛等適應症的生物學路徑
- 取得香港衛生署仿單（警語、禁忌、核准適應症）並完成安全性評估
- 針對排名較前的適應症（勃起功能障礙、偏頭痛）進行系統性文獻與臨床試驗檢索
- 確認現有劑型（牙痛滴劑、乳膏等局部製劑）與預測適應症所需給藥途徑是否相容
- 若上述檢索皆無支持證據，建議不再投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

