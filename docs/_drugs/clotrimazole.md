---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 3
---

# Clotrimazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Clotrimazole：從局部抗黴菌治療到痤瘡

## 一句話總結

Clotrimazole（克黴唑）是咪唑類抗黴菌藥，在香港有 20 張許可證，以乳膏和陰道錠等劑型上市。
TxGNN 模型預測它可能對**痤瘡 (Acne)** 有效。
目前只有 **1 個臨床試驗**，是暫停中的三合一複方試驗，**沒有文獻**支持這個方向，屬於早期、證據薄弱的預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 痤瘡 (Acne) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L4（僅有間接證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Clotrimazole 是咪唑類抗黴菌藥，抑制黴菌的羊毛固醇 14-α 去甲基酶（CYP51），使麥角固醇合成受阻，破壞黴菌細胞膜。

一種可能的關聯是，它能抑制皮脂腺毛囊單位中的馬拉色菌（Malassezia）等親脂性酵母菌，而這類菌被認為與部分痤瘡樣皮疹有關。不過，這在尋常痤瘡上**尚未被證實**。

TxGNN 的高分（99.86%）來自知識圖譜的網絡鄰近性，不是臨床證據。唯一的相關試驗使用的是 beclomethasone + gentamicin + clotrimazole 三合一複方。類固醇的抗發炎作用和抗生素都可能造成療效，因此無法分辨 clotrimazole 的貢獻。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | 暫停 | 80 | 比較 beclomethasone + gentamicin + clotrimazole 複方乳膏對受污染皮膚病（雙側對稱性病灶）的療效；未公布結果 |

此試驗為複方製劑，且題名顯示族群可能是混合性皮膚感染或皮膚炎，並非單純痤瘡，僅屬間接證據（相關性評級 C）。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-28306 | CLOTASOL CREAM 1% | EUROPHARM LAB CO LTD |
| HK-25432 | CANESTEN VAGINAL TAB 0.1G | BAYER HEALTHCARE LIMITED |
| HK-38800 | CLOTRI-DENK 100 VAGINAL TAB | STAR MEDICAL SUPPLIES LTD |
| HK-41076 | CANDINOX VAGINAL TAB 100MG | DELTAPHARM LIMITED |
| HK-45648 | CANDAZOLE CREAM 1% | TAISHO PHARMACEUTICAL (HK) LTD |

以上列出 5 張主要許可證，全部共 20 張。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 痤瘡適應症僅有一個暫停中的複方試驗，無法區分 clotrimazole 的貢獻，也沒有任何文獻，機轉關聯亦未獲證實。
- TxGNN 分數再高，也只是模型預測，不足以支持推進。

**若要推進需要：**
- 以 clotrimazole 單方對照安慰劑或標準療法的臨床試驗，且族群限定為痤瘡
- 釐清馬拉色菌或其他酵母菌在痤瘡中的角色，以及 clotrimazole 對痤瘡相關微生物的作用（機轉研究）
- 取得香港衛生署仿單，補齊警語與禁忌症資料
- 同一份預測中，**外陰陰道炎 (Vulvovaginitis)** 的證據明顯較強，有多個已完成的 RCT 與 Phase 4 對照試驗，且很可能已是仿單內的既有適應症。建議與痤瘡分開評估，並先對照仿單確認。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

