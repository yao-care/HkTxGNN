---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 899
evidence_level: L5
indication_count: 10
monitor_inn: "TRAVOPROST"
predicted_indications: ["visceral calciphylaxis", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis", "idiopathic spontaneous coronary artery dissection", "hemangioendothelioma"]
last_modified_at: 2026-10-23
description: "Travoprost：預測新適應症為內臟鈣化防禦 (Visceral Calciphylaxis)（證據等級 L5）。原適應症：開角型青光眼、高眼壓症"
---

# Travoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Travoprost：從開角型青光眼到內臟鈣化防禦（預測）
{: .text-alpha }

## 一句話總結

Travoprost 是前列腺素 F2α 類似物，原本用於**開角型青光眼 (open-angle glaucoma)** 與**高眼壓症 (ocular hypertension)**。
TxGNN 模型預測它可能對**內臟鈣化防禦 (Visceral Calciphylaxis)** 有效，但目前**沒有任何臨床試驗或文獻**直接研究這個疾病，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 開角型青光眼、高眼壓症（來自知識圖譜的記錄，香港許可證資料未載明適應症文字） |
| 預測新適應症 | 內臟鈣化防禦 (Visceral Calciphylaxis) |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 9 張／共 9 張） |
| 核准許可證數 | 9 張（有效 9 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 travoprost 是前列腺素 F2α 類似物（FP 受體促效劑），以眼部局部給藥降低眼壓。

內臟鈣化防禦屬於血管鈣化相關疾病，與青光眼在病理上沒有已知關聯。目前沒有任何試驗或文獻將 travoprost 與血管鈣化或鈣化防禦連結。此外，眼用滴劑的全身暴露量極低，機轉上難以支持此預測。高分僅代表模型的計算結果，不是臨床證據。

其他排名靠前的預測（胸廓出口症候群、胃血管發育不良、藍趾症候群、淋巴管擴張、自發性冠狀動脈剝離等）同樣沒有任何研究支持。

## 臨床試驗證據

目前無相關臨床試驗登記（針對內臟鈣化防禦）。

補充說明：排名第 5 的「血管疾病」所配對到的 10 項試驗，內容皆為青光眼或高眼壓症（眼壓控制、結膜充血、固定複方等），並非血管疾病治療研究，應是關鍵字重疊所致。其中唯一與血管相關的 NCT00308945 為小型 Phase 4 研究（n=20），僅測量視網膜血管直徑與脈絡膜血流，屬間接的眼部血流動力學資料，不能支持血管疾病適應症。

## 文獻證據

目前無相關文獻（針對內臟鈣化防禦）。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66019 | TRAVOPROST RAFARM EYE DROPS 100MCG/2.5ML | 滴眼液 | 資料未載明 |
| HK-68280 | TRAVIOP PRESERVATIVE FREE EYE DROPS SOLUTION 0.004% W/V | 滴眼液 | 資料未載明 |
| HK-65922 | TRAVOPROST NTC EYE DROPS 40MCG/ML | 滴眼液 | 資料未載明 |
| HK-67675 | TRAVOPROST-PHARMATHEN EYE DROPS 40MCG/ML | 滴眼液 | 資料未載明 |
| HK-67670 | TRAVOPROST OPHTHALMIC SOLUTION 0.004% W/V | 滴眼液 | 資料未載明 |

共 9 張有效許可證，上表僅列出 5 張。

## 安全性考量

- **知識圖譜中記錄的禁忌疾病關係（非仿單內容）**：葡萄膜炎、虹膜疾病、睫狀體疾病、全葡萄膜炎、虹膜炎、囊樣黃斑部水腫、黃斑部視網膜水腫。
- **藥物交互作用**：資料庫共記錄 49 筆，列出的項目（如 Calcitriol、Pantoprazole、Sucralfate、Morphine、Metformin、Omeprazole 等）嚴重程度皆為「未知」，無法據此判斷臨床意義。
- **個案警訊**：有一則個案報告（PMID 19107053）指出，Sturge-Weber-Krabbe 症候群（血管畸形疾病）患者使用 travoprost 後出現葡萄膜積液與滲出性視網膜剝離，對血管異常患者應謹慎。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 內臟鈣化防禦的預測僅來自模型計算，沒有任何直接研究，證據等級為 L5。
- 眼部局部給藥的全身暴露量極低，機轉上缺乏合理連結；現有血管相關資料僅為間接的眼部血流觀察，甚至有血管畸形患者的不良事件個案。

**若要推進需要：**
- 取得 travoprost 作用機轉資料，並探討 FP 受體與血管鈣化路徑是否有關聯
- 針對鈣化防禦進行前臨床或機轉研究（細胞或動物模型）
- 評估全身給藥可行性與安全性（目前僅有眼用劑型）
- 補齊香港仿單的警語與禁忌症資料
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

